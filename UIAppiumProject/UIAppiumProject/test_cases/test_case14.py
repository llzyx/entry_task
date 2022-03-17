from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from controller.basePage import basePage
import pytest
from variables import internal_destination,place_of_departure,country_index,letter_index,device_caps,module,type,route,aircraft_cabin,oversea_destination,passenger
from appium.webdriver.common.appiumby import AppiumBy
import time
#目的地为搜全国低价_查询,单程
def test_14():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp = basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()
    bp.findElement(['content_desc', route[0]]).click()

    # 选择出发地-国内
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)
    bp.findElement(['text', type[0]]).click()
    bp.findElement(['text', internal_destination[0]]).click()
    bp.findElement(['text', letter_index[2]]).click()
    bp.findElement(['text', place_of_departure[1]]).click()

    #选择目的地-全国低价
    driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)
    bp.findElement(['text', type[0]]).click()
    bp.findElement(['text',internal_destination[0]]).click()
    bp.findElement(['text','搜全国低价']).click()
    assert bp.findElement(['text', '搜全国低价']),'选择全国低价失败'

    #查询
    bp.findElement(['class', 'android.widget.Button']).click()

    #断言
    ele=bp.findElement(['content_desc','miniSearch_dcity'])
    assert ele.text==place_of_departure[1],'结果页出发城市显示错误'
    ele = bp.findElement(['content_desc', 'miniSearch_acity'])
    assert ele.text == '搜全国低价', '结果页到达城市显示错误'
    assert bp.findElement(['content_desc','cityList_city_1_image']),'搜索失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case14.py"])

