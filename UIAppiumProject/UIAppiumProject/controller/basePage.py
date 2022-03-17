#基类
from appium.webdriver.common.appiumby import AppiumBy
class basePage():
    def __init__(self,driver):
        self.driver=driver

    def findElement(self,element):
        type=element[0]
        value=element[1]
        if type=='id' or type=='Id' or type=='ID':
            ele=self.driver.find_element(AppiumBy.ID,value)
        elif type=='ACCESSIBILITY_ID' or type=='accessibility_id' or type=='content_desc':
            ele=self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,value)
        elif type=='class_name' or type=='CLASS_NAME' or type=='class':
            ele=self.driver.find_element(AppiumBy.CLASS_NAME,value)
        elif type=='xpath' or type=='Xpath' or type=='XPATH':
            ele = self.driver.find_element(AppiumBy.XPATH, value)
        elif type=='css' or type=='CSS' or type=='Css':
            ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, value)
        elif type=='text' or type=='Text' or type=='TEXT':
            code=f'UiSelector().text("{value}")'
            ele=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='text_contains' or type=='Text_Contains' or type=='TEXT_CONTAINS':
            code=f'UiSelector().textContains("{value}")'
            ele=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='text_start' or type=='Text_Start' or type=='TEXT_START':
            code=f'UiSelector().textStartsWith("{value}")'
            ele=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='resourceIdMatches' or type=='ResourceIdMatches':
            code=f'UiSelector().resourceIdMatches("{value}")'
            ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
        return ele


    def findElements(self,element):
        type=element[0]
        value=element[1]
        if type=='id' or type=='Id' or type=='ID':
            eles=self.driver.find_elements(AppiumBy.ID,value)
        elif type=='ACCESSIBILITY_ID' or type=='accessibility_id' or type=='content_desc':
            eles=self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,value)
        elif type=='class_name' or type=='CLASS_NAME' or type=='class':
            eles=self.driver.find_elements(AppiumBy.CLASS_NAME,value)
        elif type=='xpath' or type=='Xpath' or type=='XPATH':
            eles = self.driver.find_elements(AppiumBy.XPATH, value)
        elif type=='css' or type=='CSS' or type=='Css':
            eles= self.driver.find_elements(AppiumBy.CSS_SELECTOR, value)
        elif type=='text' or type=='Text' or type=='TEXT':
            code=f'UiSelector().text("{value}")'
            eles=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='text_contains' or type=='Text_Contains' or type=='TEXT_CONTAINS':
            code=f'UiSelector().textContains("{value}")'
            eles=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='text_start' or type=='Text_Start' or type=='TEXT_START':
            code=f'UiSelector().textStartsWith("{value}")'
            eles=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,code)
        elif type=='resourceIdMatches' or type=='ResourceIdMatches':
            code=f'UiSelector().resourceIdMatches("{value}")'
            eles = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, code)
        return eles