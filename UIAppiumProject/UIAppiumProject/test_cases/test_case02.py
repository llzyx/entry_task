from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from variables import device_caps,place_of_departure,address,module,type
import pytest
from controller.basePage import basePage
import time
#出发地搜索中文选择城市
def test_02():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp=basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()


    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)

    bp.findElement(['text', type[0]]).click()
    bp.findElement(['CLASS_NAME', 'android.widget.EditText']).click()
    bp.findElement(['CLASS_NAME', 'android.widget.EditText']).send_keys(place_of_departure[1])
    res = bp.findElement(['text_contains', address[0]])
    assert res, f'搜索{place_of_departure[1]}，断言失败'

    #搜索成功后选择重庆
    bp.findElement(['text_contains', address[1]]).click()
    res=bp.findElement(['text', place_of_departure[1]])
    assert res, '搜索后选择城市失败'


if __name__=='__main__':
    pytest.main(["-sv","test_case02.py"])



