from selenium import webdriver

#TODO Trang put this to .env
BROWSERSTACK_URL = 'https://trangtruong2:pgXmLCHysJEM7XrYpipy@hub-cloud.browserstack.com/wd/hub'


def load_webdriver_mswindows(browser, browser_version, name):  # mswindows aka microsoft windows os
    desired_cap = {
        'os'              : 'Windows',
        'os_version'      : '10',
        'browser'         : browser,
        'browser_version' : browser_version,
        'name'            : name
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver


def load_webdriver_macos(browser, browser_version, name):
    desired_cap = {
        'os'              : 'OS X',
        'os_version'      : 'Catalina',
        'browser'         : browser,
        'browser_version' : browser_version,
        'name'            : name
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver
