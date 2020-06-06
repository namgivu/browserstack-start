from src.service.appium_webdriver import load_appium_webdriver
from tests.util import run_googlesearchdemo

class Test:

    def test_IOS(self):
        d='iPhone XS'           ; osv='13'  ; sn='IOS test'     ; wd=load_appium_webdriver(d, osv, sn); run_googlesearchdemo(wd, tag=d)  # d aka device, osv aka os_version, sn aka session_name


    def test_android(self):
        d='Samsung Galaxy S10'  ; osv='9.0' ; sn='Android test' ; wd=load_appium_webdriver(d, osv, sn); run_googlesearchdemo(wd, tag=d)  # d aka device, osv aka os_version, sn aka session_name
