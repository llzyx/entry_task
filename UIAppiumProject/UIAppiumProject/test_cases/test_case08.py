from appium import webdriver
from controller.basePage import basePage
import pytest
from variables import internal_destination,oversea_destination,country_index,letter_index,device_caps,module,type
from appium.webdriver.common.appiumby import AppiumBy
import time

#多选4个地点
def test_08():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_caps)
  driver.implicitly_wait(5)  # 设置隐式等待时间
  bp=basePage(driver)
  bp.findElement(['ACCESSIBILITY_ID',module[0]]).click()
  time.sleep(0.5)
  bp.findElement(['text', module[0]]).click()

  width = driver.get_window_size()['width']
  height = driver.get_window_size()['height']
  driver.tap([(0.8 * width, 0.31 * height), (0.93 * width, 0.34 * height)], 300)

  # 多选4个地点
  bp.findElement(['text',type[1]]).click()
  bp.findElement(['text',country_index[0]]).click()
  bp.findElement(['text', country_index[3]]).click()
  bp.findElement(['text', oversea_destination[1]]).click()
  bp.findElement(['text', oversea_destination[2]]).click()
  bp.findElement(['text', internal_destination[0]]).click()
  bp.findElement(['text', letter_index[10]]).click()
  bp.findElement(['text', internal_destination[3]]).click()
  bp.findElement(['text', internal_destination[4]]).click()

  ##断言
  eles=bp.findElements(['XPATH','//android.widget.HorizontalScrollView[1]/android.widget.LinearLayout/android.widget.FrameLayout'])
  assert len(eles) == 3, '多选个数超过三个，断言失败'
  arr_list=[]
  texts=eles[1].find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
  arr_list.append(texts[0].text)
  texts = eles[2].find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
  arr_list.append(texts[0].text)
  texts = eles[0].find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
  arr_list.append(texts[0].text)

  if oversea_destination[1] in arr_list and oversea_destination[2] in arr_list:
    pass
  else:
    print('多选失败')


if __name__=='__main__':
    pytest.main(["-sv","test_case08.py"])







