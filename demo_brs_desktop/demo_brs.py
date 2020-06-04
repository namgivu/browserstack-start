import unittest, time, os
from selenium import webdriver

app_path = os.path.abspath(__file__ + '/../../..')

def driver(os, version, browser, browser_version, name):
    BROWSERSTACK_URL  = 'https://trangtruong2:pgXmLCHysJEM7XrYpipy@hub-cloud.browserstack.com/wd/hub'

    desired_cap       = {
        'os'              : f'{os}',
        'os_version'      : f'{version}',
        'browser'         : f'{browser}',
        'browser_version' : f'{browser_version}',
        'name'            : f'{name}'
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver

class Test:

    def test_IE(self):
        dv = driver(os='Windows', version='10', browser='IE', browser_version='11', name='IE First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/IE.png')
        dv.quit()

    def test_Edge(self):
        # TODO why can not run with Edge version 80 81
        dv = driver(os='Windows', version='10', browser='Edge', browser_version='18', name='Edge First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/Edge.png')
        dv.quit()

    def test_Firefox(self):
        dv = driver(os='Windows', version='10', browser='Firefox', browser_version='74', name='Firefox First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/Firefox.png')
        dv.quit()

    def test_Chrome(self):
        dv = driver(os='Windows', version='10', browser='Chrome', browser_version='81', name='Chrome First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/Chrome.png')
        dv.quit()

    def test_Safari(self):
        dv = driver(os='OS X', version='Catalina', browser='Safari', browser_version='13', name='Safari First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/Safari.png')
        dv.quit()

    def test_Chrome_OSX(self):
        dv = driver(os='OS X', version='Catalina', browser='Chrome', browser_version='81', name='Chrome_OSX First Test')
        dv.get('http://www.google.com')
        search_input = dv.find_element_by_name('q')
        search_input.send_keys('360f product')
        search_input.submit()

        time.sleep(3)
        dv.save_screenshot(f'{app_path}/screen_shot/Chrome_OSX.png')
        dv.quit()
