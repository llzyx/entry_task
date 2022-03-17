from appium import webdriver
import pytest
from variables import device_caps,module,letter_index,internal_destination,type
from controller.basePage import basePage
import time

#目的地选择某字母索引_选择城市
def test_06():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp=basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID',module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)

  #字母索引
  bp.findElement(['text', type[0]]).click()
  bp.findElement(['text', internal_destination[0]]).click()
  bp.findElement(['text',letter_index[6]]).click()
  res=bp.findElement(['text', internal_destination[2]])
  assert res, '选择某字母索引失败'

  #搜索后选择城市
  res.click()
  res = bp.findElement(['text', internal_destination[2]])
  assert res, '索引后选择城市失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case06.py"])


