from src.service.webdriver import load_webdriver_mswindows, load_webdriver_macos
from tests.util import run_googlesearchdemo

class Test:

    def test_IE(self):                                                 # :name aka what BRS used to named for testcase on BRS_dashboard ref. doc/why-param-name-when-creating-wd.png
        wd = load_webdriver_mswindows(browser='IE', browser_version='11', name='IE First Test')  # wd aka webdriver
        run_googlesearchdemo(wd, 'IE')

    def test_Edge(self):
        # TODO why can not run with Edge version 80 81
        wd = load_webdriver_mswindows(browser='Edge', browser_version='18', name='Edge First Test')
        run_googlesearchdemo(wd, 'Edge')

    def test_Firefox(self):
        wd = load_webdriver_mswindows(browser='Firefox', browser_version='74', name='Firefox First Test')
        run_googlesearchdemo(wd, 'Firefox')

    def test_Chrome(self):
        wd = load_webdriver_mswindows(browser='Chrome', browser_version='81', name='Chrome First Test')
        run_googlesearchdemo(wd, 'Chrome')

    def test_Safari(self):
        wd = load_webdriver_macos(browser='Safari', browser_version='13', name='Safari First Test')
        run_googlesearchdemo(wd, 'Safari')

    def test_Chrome_OSX(self):
        wd = load_webdriver_macos(browser='Chrome', browser_version='81', name='Chrome_OSX First Test')
        run_googlesearchdemo(wd, 'Chrome_OSX')
