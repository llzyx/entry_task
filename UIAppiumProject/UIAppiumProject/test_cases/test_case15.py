from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from controller.basePage import basePage
import pytest
from variables import internal_destination,place_of_departure,country_index,letter_index,device_caps,module,type,route,aircraft_cabin,oversea_destination,passenger
from appium.webdriver.common.appiumby import AppiumBy
import time
#出发地、目的地均为多个地点
def test_15():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp = basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()
    bp.findElement(['content_desc', route[0]]).click()

    #出发地为多个
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)
    bp.findElement(['text', type[1]]).click()
    bp.findElement(['text', internal_destination[0]]).click()
    bp.findElement(['text',letter_index[1]]).click()
    bp.findElement(['text',place_of_departure[2]]).click()
    bp.findElement(['class','android.widget.Button']).click()

    #自动切换为特价机票查询页面
    assert bp.findElement(['text','查询特价']),'多选地点未跳转到特价查询页面'
    time.sleep(0.5)

    #目的地为多个
    driver.tap([(0.7 * width, 0.32 * height), (0.93 * width, 0.35 * height)], 300)
    bp.findElement(['text', country_index[0]]).click()
    bp.findElement(['text',country_index[3]]).click()
    bp.findElement(['text', oversea_destination[1]]).click()
    bp.findElement(['class', 'android.widget.Button']).click()

    # 查询
    bp.findElement(['class', 'android.widget.Button']).click()

    #断言
    assert bp.findElement(['content_desc','dCityNames']),'多地点查询失败'
    assert bp.findElement(['content_desc', 'aCityNames']), '多地点查询失败'


if __name__=='__main__':
    pytest.main(["-sv","test_case15.py"])



