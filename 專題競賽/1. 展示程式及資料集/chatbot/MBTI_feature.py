def mbti_feature( MBTI ):
    mbti = {}
    if MBTI == 'ISTP':
        mbti['ename'] = 'ISTP'
        mbti['cname'] = '鑒賞家'
        mbti['feature'] = '大膽且實際的實驗者，擅長使用各種工具'
        mbti['url'] = 'https://i.pinimg.com/474x/3f/3a/46/3f3a46265d52377f68ce97ef6b973cf6.jpg'
    elif MBTI == 'ISFP':
        mbti['ename'] = 'ISFP'
        mbti['cname'] = '探險家'
        mbti['feature'] = '靈動有魅力的藝術家，隨時準備著探索和體驗新事物'
        mbti['url'] = 'https://i.pinimg.com/474x/08/3b/6b/083b6bdad239a229e17e806be290e22f.jpg'
        
    elif MBTI == 'ESTP':
        mbti['ename'] = 'ESTP'
        mbti['cname'] = '企業家'
        mbti['feature'] = '精明、精力充沛且非常有觀察力，他們通常熱衷於衝鋒陷陣'
        mbti['url'] = 'https://i.pinimg.com/474x/ae/26/d1/ae26d182a759f1090ce11d498c312142.jpg'
        
    elif MBTI == 'ESFP':
        mbti['ename'] = 'ESFP'
        mbti['cname'] = '表演者'
        mbti['feature'] = '精力充沛，熱情並會心血來潮，在他們身邊永遠不會無聊'
        mbti['url'] = 'https://i.pinimg.com/474x/50/22/5a/50225af2fac591a0dfa0821280f35d47.jpg'

    elif MBTI == 'INTP':
        mbti['ename'] = 'INTP'
        mbti['cname'] = '邏輯學家'
        mbti['feature'] = '創新的發明家，對知識充滿無法抑制的執著'
        mbti['url'] = 'https://i.pinimg.com/474x/94/31/0d/94310d7e94eccb56b8caafcfe040c6a8.jpg'
    
    elif MBTI == 'INTJ':
        mbti['ename'] = 'INTJ'
        mbti['cname'] = '建築師'
        mbti['feature'] = '富有想像力和策略思想，掌握所有的計畫'
        mbti['url'] = 'https://i.pinimg.com/474x/28/3d/e2/283de2940b98e457721bdc9a7e1ae245.jpg'
        
    elif MBTI == 'ENTP':
        mbti['ename'] = 'ENTP'
        mbti['cname'] = '辯論家'
        mbti['feature'] = '聰明且好奇的思想者，無法抵擋智力挑戰的誘惑'
        mbti['url'] = 'https://i.pinimg.com/474x/2b/8b/e5/2b8be5eedf1ef3760b2571e16c5e71e2.jpg'
        
    elif MBTI == 'ENTJ':
        mbti['ename'] = 'ENTJ'
        mbti['cname'] = '指揮官'
        mbti['feature'] = '領導者大膽、富有想像力愜意志強大，隨時都有辦法或創造解決方案'
        mbti['url'] = 'https://i.pinimg.com/474x/2d/eb/a9/2deba9060dc3049ea3ccef60d41860a5.jpg'
        
    elif MBTI == 'ISTJ':
        mbti['ename'] = 'ISTJ'
        mbti['cname'] = '物流師'
        mbti['feature'] = '務實且注重事實思考的個人，可靠性不容懷疑'
        mbti['url'] = 'https://i.pinimg.com/474x/81/f9/90/81f990e5539218bc89a3fc1fdf071da3.jpg'
        
    elif MBTI == 'ISFJ':
        mbti['ename'] = 'ISFJ'
        mbti['cname'] = '守衛者'
        mbti['feature'] = '非常敬業和熱情的保護者，隨時準備保護他們所愛的人'
        mbti['url'] = 'https://i.pinimg.com/474x/30/82/a3/3082a3e5af1d8d3239da6046eef5e731.jpg'
        
    elif MBTI == 'ESTJ':
        mbti['ename'] = 'ESTJ'
        mbti['cname'] = '總經理'
        mbti['feature'] = '出色的管理者，管理事務或人員得心應手'
        mbti['url'] = 'https://i.pinimg.com/474x/10/fa/74/10fa74c59f7964452bb5952f9a34d6c9.jpg'
        
    elif MBTI == 'ESFJ':
        mbti['ename'] = 'ESFJ'
        mbti['cname'] = '執政官'
        mbti['feature'] = '非常關心他人，善於社交且受人歡迎，總是樂於助人'
        mbti['url'] = 'https://i.pinimg.com/474x/36/00/c3/3600c3ce31e99d7d8e75f0299db3c16e.jpg'
        
    elif MBTI == 'INFJ':
        mbti['ename'] = 'INFJ'
        mbti['cname'] = '提倡者'
        mbti['feature'] = '沉靜有遠見的人，通常是鼓舞人心且從不會感到疲倦的理想主義者'
        mbti['url'] = 'https://i.pinimg.com/474x/ab/b4/34/abb4346095cba482298f0e493752201b.jpg'
        
    elif MBTI == 'INFP':
        mbti['ename'] = 'INFP'
        mbti['cname'] = '調停者'
        mbti['feature'] = '富有詩意，善良無私的人，總是熱情協調正義的事'
        mbti['url'] = 'https://i.pinimg.com/474x/89/0f/34/890f340dd42c917372f5e9cb60b90e23.jpg'

    elif MBTI == 'ENFJ':
        mbti['ename'] = 'ENFJ'
        mbti['cname'] = '主人公'
        mbti['feature'] = '領導者具有個人魅力並能激勵人心，讓聽眾為之著迷'
        mbti['url'] = 'https://i.pinimg.com/474x/90/5b/db/905bdbe026d340d9d0777d83d5b9a583.jpg'

    elif MBTI == 'ENFP':
        mbti['ename'] = 'ENFP'
        mbti['cname'] = '競選者'
        mbti['feature'] = '充滿活力，富有創意，善於交際的自由精神，隨時展現友善的微笑'
        mbti['url'] = 'https://i.pinimg.com/474x/a1/af/bf/a1afbf68e2b23d32a6464c143fa822de.jpg'
        
    return mbti
