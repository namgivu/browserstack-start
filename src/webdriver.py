from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME      = os.environ.get('USERNAME')
AUTOMATE_KEY  = os.environ.get('AUTOMATE_KEY')
BROWSERSTACK_URL = f'https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub'

def load_webdriver_mswindows(browser, browser_version, name):  # mswindows aka microsoft windows os
    desired_cap = {
        'os'              : 'Windows',
        'os_version'      : '10',
        'browser'         : browser,
        'browser_version' : browser_version,
        'name'            : name,
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
        'name'            : name,
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver
