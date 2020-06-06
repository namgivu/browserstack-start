from selenium import webdriver
import os
from dotenv import load_dotenv

APP_HOME = os.path.abspath(__file__ + '/../../..')

#region load .env file
env_f=f'{APP_HOME}/.env'
if not os.path.isfile(env_f): raise Exception(f'Not found .env at {env_f} - please clone one from {APP_HOME}/.env_vault/.env.xxx')
else:                         load_dotenv(dotenv_path=env_f, override=True)
#endregion


# load BROWSERSTACK_URL
USERNAME         = os.environ.get('USERNAME')
AUTOMATE_KEY     = os.environ.get('AUTOMATE_KEY')
BROWSERSTACK_URL = f'https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub'

#                                                     :session_name is what brs used to named for testcase on brs dashboard ref. doc/why-param-name-when-creating-wd.png  # brs aka browserstack
def load_webdriver_win10(browser, browser_version, session_name):
    desired_cap = {
        'os'              : 'Windows',
        'os_version'      : '10',

        'browser'         : browser,
        'browser_version' : browser_version,

        'name'            : session_name,
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(6)
    return driver


def load_webdriver_osx(browser, browser_version, session_name):
    desired_cap = {
        'os'              : 'OS X',
        'os_version'      : 'Catalina',

        'browser'         : browser,
        'browser_version' : browser_version,

        'name'            : session_name,
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(6)
    return driver
