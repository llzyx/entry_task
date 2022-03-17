from appium import webdriver
from controller.basePage import basePage
from variables import country_index,oversea_destination,module,device_caps,type
import pytest
import time

#目的地选择国际->东南亚—>曼谷
def test_07():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp=basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID',module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)

  #选择国际->东南亚—>曼谷
  bp.findElement(['text', type[0]]).click()
  bp.findElement(['text',country_index[0]]).click()
  bp.findElement(['text',country_index[2]]).click()
  bp.findElement(['text',oversea_destination[0]]).click()

  #断言
  res = bp.findElement(['text',oversea_destination[0]])
  assert res, '选择国际城市失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case07.py"])







