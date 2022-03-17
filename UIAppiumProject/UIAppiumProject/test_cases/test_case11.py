from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from controller.basePage import basePage
import pytest
from variables import internal_destination,place_of_departure,country_index,letter_index,device_caps,module,type,route,aircraft_cabin,oversea_destination
from appium.webdriver.common.appiumby import AppiumBy

#单程、出发地为国内、目的地为国际、经济舱、超级经济舱，乘机人类型为1成人1儿童
def test_11():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
    driver.implicitly_wait(5)  # 设置隐式等待时间
    bp = basePage(driver)
    bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
    time.sleep(0.5)
    bp.findElement(['text', module[0]]).click()
    bp.findElement(['content_desc',route[0]]).click()

    #选择出发地-国内
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)
    bp.findElement(['text',type[0]]).click()
    bp.findElement(['text',internal_destination[0]]).click()
    bp.findElement(['text',letter_index[2]]).click()
    bp.findElement(['text',place_of_departure[1]]).click()

    #选择目的地-国际
    driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)
    bp.findElement(['text',type[0]]).click()
    bp.findElement(['text', country_index[0]]).click()
    bp.findElement(['text', country_index[2]]).click()
    bp.findElement(['text', oversea_destination[0]]).click()

    #选择时间,难点：无法定位具体时间，待解决，目前是随机时间


    #选择经济舱、超级经济舱
    #driver.tap([(0.068 * width, 0.44 * height), (0.44 * width, 0.46 * height)],300)
    # eles=bp.findElements(['class','android.widget.ListView'])
    # eles[0].click()

    #选择乘车人类型，难点：无法定位到弹窗，待解决，目前使用默认
    #driver.tap([(0.67 * width, 0.44 * height), (0.91 * width, 0.46 * height)], 300)


    #查询
    bp.findElement(['class','android.widget.Button']).click()



    #断言是否跳转到结果页面
    bp.findElement(['content_desc','公告弹框确认按钮1']).click()
    ele=bp.findElement(['content_desc','列表页头部出发城市'])
    assert ele.text==place_of_departure[1],'航班的出发城市错误'
    ele1 = bp.findElement(['content_desc','列表页头部到达城市'])
    assert ele1.text == oversea_destination[0], '航班的到达城市错误'
    # if bp.findElement(['content_desc','第1条航班']):
    #     pass
    # elif bp.findElement(['text','未找到符合条件的航班']):
    #     pass
    # else:
    #     print('查询失败')


if __name__=='__main__':
    pytest.main(["-sv","test_case11.py"])








