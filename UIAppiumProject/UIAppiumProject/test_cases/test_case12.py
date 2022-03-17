from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from controller.basePage import basePage
import pytest
from variables import internal_destination,place_of_departure,country_index,letter_index,device_caps,module,type,route,aircraft_cabin,oversea_destination,passenger
from appium.webdriver.common.appiumby import AppiumBy

#往返、出发地、目的地为国内、头等舱，带儿童
def test_12():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp = basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()
    bp.findElement(['content_desc',route[1]]).click()

    #选择出发地-国内
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)
    bp.findElement(['text',type[0]]).click()
    bp.findElement(['text',internal_destination[0]]).click()
    bp.findElement(['text',letter_index[2]]).click()
    bp.findElement(['text',place_of_departure[1]]).click()

    # 选择目的地-国内
    driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)
    bp.findElement(['text', type[0]]).click()
    bp.findElement(['text', internal_destination[0]]).click()
    bp.findElement(['text', letter_index[6]]).click()
    bp.findElement(['text', internal_destination[2]]).click()

    #选择时间,难点：无法定位具体时间，待解决，目前是随机时间


    #选择头等舱
    bp.findElement(['text',aircraft_cabin[1]]).click()

    #选择乘车人类型，带儿童
    bp.findElement(['text',passenger[0]]).click()

    #查询
    bp.findElement(['class','android.widget.Button']).click()



    #断言是否跳转到结果页面
    ele=bp.findElement(['content_desc','列表页头部出发城市'])
    assert ele.text==place_of_departure[1],'航班的出发城市错误'
    ele1 = bp.findElement(['content_desc','列表页头部到达城市'])
    assert ele1.text == internal_destination[2], '航班的到达城市错误'
    if bp.findElement(['content_desc','去程第1条航班']):
        assert bp.findElement(['text','公务/头等舱']),'结果页显示舱位错误'
        driver.swipe(start_x=700, start_y=1000, end_x=50, end_y=1000, duration=1000)
        assert bp.findElement(['content_desc','返程第1条航班']),'显示返程航班错误'
    elif bp.findElement(['text','未找到符合条件的航班']):
        pass
    else:
        print('查询失败')


if __name__=='__main__':
    pytest.main(["-sv","test_case12.py"])








