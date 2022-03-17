device_caps={
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '10',  # 手机安卓版本
            'deviceName': '小米9',  # 设备名，安卓手机可以随意填写
            'appPackage': 'ctrip.android.view',  # 启动APP Package名称
            'appActivity': 'ctrip.business.splash.CtripSplashActivity',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': True,  # 不要重置App
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
        }

module=['机票']
type=['单选','多选']
route=['单程','往返']
aircraft_cabin=['经济舱','公务/头等舱','经济舱、超级经济舱']
passenger=['带儿童','带婴儿']
place_of_departure=['chongqing','重庆','百色']
letter_index=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
internal_destination=['国内','guangzhou','广州','喀什','康定']
address=['重庆 中国','重庆 CKG','白云机场 广东 CAN']
country_index=['国际/中国港澳台','中国港澳台','东南亚','日韩','欧洲','美洲','亚洲其他','大洋洲','非洲','精选海岛']
oversea_destination=['曼谷','东京','首尔']