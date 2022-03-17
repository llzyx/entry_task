from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from variables import device_caps,letter_index,place_of_departure,module,internal_destination,type
from controller.basePage import basePage
import pytest
import time

#出发地索引选择城市
def test_03():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp = basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID', module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.07 * width, 0.31 * height), (0.31 * width, 0.34 * height)], 300)

  bp.findElement(['text', type[0]]).click()
  bp.findElement(['text',internal_destination[0]]).click()
  bp.findElement(['text', letter_index[2]]).click()
  res = bp.findElement(['text', place_of_departure[1]])
  assert res, '选择某字母索引失败'

  # 索引后选择城市
  res.click()
  res1 = bp.findElement(['text', place_of_departure[1]])
  assert res1, '索引后选择城市失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case03.py"])




