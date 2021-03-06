from appium import webdriver
import os
from dotenv import load_dotenv

APP_HOME = os.path.abspath(__file__ + '/../../..')

#region load .env file
env_f=f'{APP_HOME}/.env'
if os.path.isfile(env_f) is False: raise Exception(f'Not found .env at {env_f} - please clone one from {APP_HOME}/.env_vault/.env.xxx')
else:                              load_dotenv(dotenv_path=env_f, override=True)
#endregion


# load BROWSERSTACK_URL
USERNAME         = os.environ.get('USERNAME')
AUTOMATE_KEY     = os.environ.get('AUTOMATE_KEY')
BROWSERSTACK_URL = f'https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub'


#                                          :session_name is what brs used to named for testcase on brs dashboard ref. doc/why-param-name-when-creating-wd.png  # brs aka browserstack
def load_appium_webdriver(device, os_version, session_name):
    desired_cap = {
        'realMobile'  : True,
        'device'      : device,
        'os_version'  : os_version,

        'name'        : session_name
    }

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    driver.implicitly_wait(5)
    return driver
