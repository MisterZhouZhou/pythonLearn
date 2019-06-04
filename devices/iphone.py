# coding:utf-8

from appium import webdriver

cap = {
    'platformName': 'iOS',
    'platformVersion': '11.4',
    'deviceName': 'iPhone 7',
    'browerName': 'safari'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.get('https://m.baidu.com')