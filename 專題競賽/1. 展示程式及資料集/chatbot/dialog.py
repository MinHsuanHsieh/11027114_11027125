import json
import inspect
from linebot.models import TextSendMessage, StickerSendMessage
import re
import copy
from requests.exceptions import ReadTimeout
import global_variable as gv





class User:

    def __init__(self, userID: str):
        self.userID = userID
        self.state: int = '主選單'
        """正在使用的功能, 初始為主選單"""
        self.current_input = None
        """最近一次的輸入內容"""
        self.waiting_for = None
        """正在等待的參數名稱, None表示不在等待狀態"""
        self.args: dict = {}
        """所需要的參數"""
        self.global_args: dict = {}
        """全域變數"""

        self.abandoned = False
        if gv.SESSION.exists(userID):
            value = gv.SESSION.get(userID)
            attrs = json.loads(value)
            for k, v in attrs.items():
                setattr(self, k, v)

    def clear(self):
        self.state: int = '主選單'
        self.waiting_for = None
        self.args: dict = {}

    def __repr__(self) -> str:
        return self.__dict__.__str__()

    def dump(self):
        if self.abandoned:
            gv.SESSION.delete(self.userID)
        else:
            gv.SESSION.set(self.userID, json.dumps(self.__dict__))


    def clear_user_global_args(self, function_name):
        for parameter in self.global_args[function_name]:
            self.global_args[function_name][parameter] = []

    @staticmethod
    def clear_all():
        gv.SESSION.flushdb()

User.clear_all()


class Sub_Function:
    def __init__(self, function_name: str):
        self.function_name = function_name


class Dialog_Manager:
    _developer_functions = set()
    _callback_map = {}
    _re_map = {}
    _QA_map = {}
    _global_args_map = {}
    current_user: User = None
    user_log = []
    isCommand = False


    @staticmethod
    def __collect_parameters(user: User, message: str):
        if user.waiting_for is not None:
            user.args[user.waiting_for] = message

        for parameter in Dialog_Manager._callback_map[user.state]['parameters']:
            if parameter not in user.args:
                user.waiting_for = parameter
                return Dialog_Manager._callback_map[user.state]['parameters'][parameter]
        user.waiting_for = None
        return None

    @staticmethod
    def reply(userID: str, message: str):
        reply_array = []
        try:
            user = User(userID)
            gv.g.current_user = user
            user.current_input = message
            Dialog_Manager.isCommand = False
            
            # 初始化全域變數
            if user.global_args == {}:
                user.global_args = copy.deepcopy(Dialog_Manager._global_args_map)

            # 解碼使用者輸入
            for key, value in Dialog_Manager._re_map.items():
                if value.match(message):
                    message = key
                    break

            # 初始狀態
            if user.state == '主選單':
                isFunction = False
                if message in Dialog_Manager._callback_map:
                    isFunction = True
                if isFunction:
                    user.state = message
                    Dialog_Manager.isCommand = True
                else:
                    reply_array.append([TextSendMessage(text='暫無此功能')])
                    return reply_array

            # 允許從參數收集階段跳回主選單
            if user.waiting_for is not None and (message in Dialog_Manager._callback_map or message == '主選單'):
                user.clear()
                user.state = message
                Dialog_Manager.isCommand = True
                if user.state == '主選單':
                    user.dump()
                    return reply_array

            # 執行參數收集
            return_msg = Dialog_Manager.__collect_parameters(user, message)
            if return_msg is not None:
                msg = []
                for i in return_msg:
                    if callable(i):
                        msg.append(i())
                    else:
                        msg.append(i)
                reply_array.append(msg)

            # 參數收集完畢，執行程式
            if user.state != '主選單' and user.waiting_for is None:
                try:
                    result = Dialog_Manager._callback_map[user.state]['function'](**user.args)
                    if result is None or result == []:
                        reply_array.append([TextSendMessage(text='暫無此功能')])
                    elif result == 'abandon':
                        pass
                    else:
                        reply_array.append(result)
                        
                    if user.waiting_for is None:
                        user.clear()

                except Exception as e:
                    print(e)
                    user.clear()
                    reply_array.append([TextSendMessage(text="系統發生錯誤，已將錯誤回報給開發人員")])
                    reply_array.append([StickerSendMessage(package_id=6136, sticker_id=10551379)])

            user.dump()
        except ReadTimeout as e:
            return reply_array
        return reply_array

    @staticmethod
    def __get_parameter(name: str, default, parameter: dict):
        if name in parameter:
            return parameter[name]
        return default

    @staticmethod
    def bind(function_name: str, *args, **kwargs):
        """將function與對話綁定\n\nfunction_name: 要綁定的功能名稱, 會顯示於Line選單上\n\n*args: 要求使用者輸入對應參數時所傳送的文字 ex: '請輸入身高', '請輸入體重', ...\n\n**kwargs: 附加選項 ex: re=True"""

        def decorator(func, function_name: str, *args, **kwargs):
            param_list = list(inspect.signature(func).parameters)
            if len(param_list) < len(args):
                raise ValueError('參數設定錯誤')
            parameter_map = {}
            for i in range(len(args)):
                parameter_map[param_list[i]] = args[i]
            map = {'function': None, 'parameters': None}
            map['function'] = func
            map['parameters'] = parameter_map

            if Dialog_Manager.__get_parameter('re', False, kwargs):
                Dialog_Manager._re_map[function_name] = re.compile(function_name)
            Dialog_Manager._callback_map[function_name] = map

            return func
        return lambda func: decorator(func, function_name, *args, **kwargs)

    @staticmethod
    def set_global_args(function_name: str, parameter: str, value=None):
        if function_name not in Dialog_Manager._global_args_map:
            Dialog_Manager._global_args_map[function_name] = {}
        Dialog_Manager._global_args_map[function_name][parameter] = value

    @staticmethod
    def get_global_args(function_name: str, parameter: str):
        # 獲取指定的全域變數，如果不存在則返回 None
        return Dialog_Manager._global_args_map.get(function_name, {}).get(parameter)