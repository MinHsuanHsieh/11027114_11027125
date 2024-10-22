import time
import imapclient
import email
from email.policy import default
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import re

def chrome():
    # 指定 Chrome 驅動程序的路徑
    #chromedriver_path = '/home/cynthia/chat_bot/chromedriver-linux64/chromedriver'  # 替換為你的實際路徑

    # 創建 Chrome 選項
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 添加無頭模式選項
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速，某些情況下可能需要
    chrome_options.add_argument("--no-sandbox")  # 在沙盒模式下運行 Chrome，提高安全性
    chrome_options.add_argument("--disable-dev-shm-usage")  # 解決 DevToolsActivePort 文件不存在的問題

    # 創建 Service 對象
    service = Service(ChromeDriverManager().install())

    # 使用 Service 對象和 Chrome 選項創建 WebDriver 實例
    browser = webdriver.Chrome(service=service, options=chrome_options)
    return browser

def open_spotify(browser):
    try:
        # 打開 Spotify 登入頁面
        browser.get('https://developer.spotify.com/')


        # 點擊登入按鈕
        login_button = browser.find_element(By.XPATH, '//*[@id="__next"]/div/header/div[3]/nav/div/ul/li[3]/button')
        browser.execute_script("arguments[0].click();", login_button)
        # 等待頁面加載並找到輸入電子郵件地址的輸入框
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'login-username'))
        )
        email_input.send_keys('kikikig14@gmail.com')  # 替換為你的電子郵件地址

        # 輸入密碼
        password_input = browser.find_element(By.ID, 'login-password')
        password_input.send_keys('Tt338833887')  # 替換為你的密碼

        # 使用 JavaScript 點擊記住我選項
        #remember_me = browser.find_element(By.XPATH, '//input[@id="login-remember"]')
        #browser.execute_script("arguments[0].click();", remember_me)

        # 點擊登入按鈕
        login_button = browser.find_element(By.XPATH, '//button[@id="login-button"]')
        browser.execute_script("arguments[0].click();", login_button)
        time.sleep(5)

        # 從郵箱獲取驗證碼
        def get_verification_code(myemail, password):
            try:
                time.sleep(2)
                # 連接到IMAP服務器
                server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
                server.login(myemail, password)

                # 選擇收件箱
                server.select_folder('INBOX', readonly=True)

                # 搜索含有驗證碼的郵件
                messages = server.search(['FROM', 'no-reply@alerts.spotify.com'])
                latest_message_id = messages[-1]  # 假設最新的郵件是驗證碼郵件

                # 獲取郵件內容
                raw_message = server.fetch([latest_message_id], ['BODY[]', 'FLAGS'])
                raw_email = raw_message[latest_message_id][b'BODY[]']
                msg = email.message_from_bytes(raw_email, policy=default)

                # 假設驗證碼在郵件的正文中
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            text = part.get_payload(decode=True).decode(part.get_content_charset())
                            break
                else:
                    text = msg.get_payload(decode=True).decode(msg.get_content_charset())
                
                pattern = r'(?<=請輸入或複製貼上安全碼：\r\n\r\n\r\n)\d+(?=\r\n\r\n\r\n此代碼將於 20 分鐘後失效)'
                match = re.search(pattern, text)
                if match:
                    # 提取匹配的安全碼
                    security_code = match.group(0)
                    return security_code
                else:
                    print('未找到安全碼')

                return verification_code
            except Exception as e:
                print(f"An error occurred: {e}")


        try:
            verification_code = get_verification_code('kikikig14@gmail.com', 'srtn lzgh qhzs zveh')  # 替換為你的郵箱和密碼
            
            # 在Spotify驗證碼輸入框中輸入驗證碼
            auth_code_input = browser.find_element(By.XPATH, '//*[@id="輸入我們傳送給你的 {pinLength} 位數驗證碼以確認你的電子郵件"]')
            auth_code_input.send_keys(verification_code)

            # 提交驗證碼
            submit_code_button = browser.find_element(By.XPATH, '//*[@id="encore-web-main-content"]/div/div/div/div/form/div/div[2]/button')
            browser.execute_script("arguments[0].click();", submit_code_button)
            print('Verification code submitted successfully!')
        except Exception as e:
            pass

        # 等待登入完成，並進入目標頁面
        Dashbord = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/header/div[3]/nav/div/ul/li[3]/a'))  # 替換為實際的元素ID或XPath
        )
        browser.execute_script("arguments[0].click();", Dashbord)
        time.sleep(1)
        hhmusic = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[2]/ul/li/div[2]/div/h2/a')
        browser.execute_script("arguments[0].click();", hhmusic)
        time.sleep(1)
        setting = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/a')
        browser.execute_script("arguments[0].click();", setting)
        time.sleep(1)
        User_manage = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[3]/section/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", User_manage)
        return browser

    except TimeoutException as e:
        print(f"TimeoutException: {e}")
    except ElementClickInterceptedException as e:
        print(f"ElementClickInterceptedException: {e}")

    
def email_spotify(browser, useremail, lineID):

    # 等待頁面加載，並找到填寫使用者全名和電子郵件地址的輸入框
    full_name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))  # 替換為實際的元素ID或XPath
    )
    full_name_input.send_keys(lineID)  # 替換為你的全名

    email_input = browser.find_element(By.XPATH, '//*[@id="email"]')  # 替換為實際的元素ID或XPath
    email_input.send_keys(useremail)  # 替換為你的電子郵件地址

    # 點擊提交按鈕
    submit_button = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[4]/div/div/div[2]/form/div/div[3]/button/span[1]')  # 替換為實際的元素ID或XPath
    browser.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)

    print('Submitted successfully!')

def delete_spotify(browser):
    # 抓取所有資料列，確認是否超過10筆
    try:                 
        rows = browser.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[4]/div/div/div[3]/div/table/tbody/tr[10]/td[1]')  # 替換為實際資料列的XPath
        if rows:      
            delete_dot = browser.find_element(By.XPATH, f'//*[@id="main"]/div/div/div[4]/div/div/div[3]/div/table/tbody/tr[1]/td[5]/div/div/button')  # 替換為實際的元素XPath
            browser.execute_script("arguments[0].click();", delete_dot)
            
            delete_button = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/ul/li/button')  # 替換為實際的元素ID或XPath
            browser.execute_script("arguments[0].click();", delete_button)
            print('Deleted successfully!')
        else:
            print(f"No need to delete.")
            
    except Exception as e:
        print(f"No need to delete.")

def main():
    email = 'hi@gmail.com'
    lineID = 'hi'
    browser = chrome()
    open_spotify(browser)
    time.sleep(5)
    email_spotify(browser, email, lineID)
    number = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[4]/div/div/div[2]/span/text()[1]')
    if number == 20:
        delete_spotify(browser)

if __name__ == '__main__':
    main()