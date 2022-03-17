from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from controller.basePage import basePage
from variables import place_of_departure,device_caps,address,module,type
import pytest
import time

#出发地搜索拼音
def test01():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp = basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()

    # 获取手机的分辨率
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)

    bp.findElement(['text',type[0]]).click()
    bp.findElement(['CLASS_NAME', 'android.widget.EditText']).click()
    bp.findElement(['CLASS_NAME', 'android.widget.EditText']).send_keys(place_of_departure[0])
    res = bp.findElement(['text_contains', address[0]])
    assert res, f'搜索{place_of_departure[0]}，断言失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case01.py"])

# width=driver.get_window_size()['width']
# height=driver.get_window_size()['height']
# driver.tap([(0.07*width,0.31*height),(0.31*width,0.34*height)],300)
# driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText').click()
# driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText').send_keys('chongqing')
# code='UiSelector().textContains("重庆 中国")'
# res=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
# assert res,'搜索chongqing，断言失败'

