from appium import webdriver
from controller.basePage import basePage
import pytest
from variables import internal_destination,oversea_destination,country_index,letter_index,device_caps,module,type
from appium.webdriver.common.appiumby import AppiumBy
import time

#选择3个地点_删除一个地点_再新增一个地点
def test_09():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp=basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID',module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)

  # 先选3个地点
  bp.findElement(['text',type[1]]).click()
  bp.findElement(['text',country_index[0]]).click()
  bp.findElement(['text', country_index[3]]).click()
  bp.findElement(['text', oversea_destination[1]]).click()
  bp.findElement(['text', oversea_destination[2]]).click()
  bp.findElement(['text', internal_destination[0]]).click()
  bp.findElement(['text', letter_index[10]]).click()
  bp.findElement(['text', internal_destination[3]]).click()

  #删除一个地点
  eles = bp.findElements(
    ['XPATH', '//android.widget.HorizontalScrollView[1]/android.widget.LinearLayout/android.widget.FrameLayout'])
  texts = eles[2].find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
  texts[0].click()

  eles = bp.findElements(
    ['XPATH', '//android.widget.HorizontalScrollView[1]/android.widget.LinearLayout/android.widget.FrameLayout'])
  assert len(eles),'删除一个地点失败'

  #新增一个地点
  bp.findElement(['text', internal_destination[0]]).click()
  bp.findElement(['text', letter_index[10]]).click()
  bp.findElement(['text', internal_destination[3]]).click()

  ##断言
  eles=bp.findElements(['XPATH','//android.widget.HorizontalScrollView[1]/android.widget.LinearLayout/android.widget.FrameLayout'])
  assert len(eles) == 3, '多选个数超过三个，断言失败'
  texts=eles[2].find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
  assert texts[0].text == f'{internal_destination[3]}', '多选城市错误'


if __name__=='__main__':
    pytest.main(["-sv","test_case09.py"])







