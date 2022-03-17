from appium import webdriver
import pytest
from variables import device_caps,internal_destination,module,address,type
from controller.basePage import basePage
import time

#目的地搜索拼音
def test_04():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp=basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID',module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)

  #目的地搜索guangzhou
  bp.findElement(['text', type[0]]).click()
  bp.findElement(['CLASS_NAME','android.widget.EditText']).click()
  bp.findElement(['CLASS_NAME', 'android.widget.EditText']).send_keys(internal_destination[1])
  res=bp.findElement(['text_contains',address[2]])
  assert res, f'搜索{internal_destination[1]}，断言失败'

if __name__=='__main__':
    pytest.main(["-sv","test_case04.py"])

