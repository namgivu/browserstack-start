from selenium import webdriver

BROWSERSTACK_URL = 'https://trangtruong2:pgXmLCHysJEM7XrYpipy@hub-cloud.browserstack.com/wd/hub'


def windows_driver(browser, browser_version, name):
    desired_cap       = {
        'os'              : 'Windows',
        'os_version'      : '10',
        'browser'         : browser,
        'browser_version' : browser_version,
        'name'            : name
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver


def osx_driver(browser, browser_version, name):
    desired_cap       = {
        'os'              : 'OS X',
        'os_version'      : 'Catalina',
        'browser'         : browser,
        'browser_version' : browser_version,
        'name'            : name
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver
