from src.service.appium_webdriver import load_webdriver_android, load_webdriver_ios
from tests.util import run_googlesearchdemo

class Test:

    def test_IOS(self):
        wd = load_webdriver_ios(device='iPhone XS', os_version='13', session_name='IOS test')
        run_googlesearchdemo(wd, 'IOS')

    def test_android(self):
        wd = load_webdriver_android(device='Samsung Galaxy S10', os_version='9.0', session_name='Android test')
        run_googlesearchdemo(wd, 'Android')
