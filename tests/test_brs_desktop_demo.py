from src.service.webdriver import load_webdriver_win10, load_webdriver_osx
from tests.util import run_googlesearchdemo

class Test:

    def test_IE(self):
        wd = load_webdriver_win10(browser='IE', browser_version='11', session_name='IE First Test')  # wd aka webdriver
        run_googlesearchdemo(wd, 'IE')

    def test_Edge(self):
        # TODO why can not run with Edge version 80 81
        wd = load_webdriver_win10(browser='Edge', browser_version='18', session_name='Edge First Test')
        run_googlesearchdemo(wd, 'Edge')

    def test_Firefox(self):
        wd = load_webdriver_win10(browser='Firefox', browser_version='74', session_name='Firefox First Test')
        run_googlesearchdemo(wd, 'Firefox')

    def test_Chrome(self):
        wd = load_webdriver_win10(browser='Chrome', browser_version='81', session_name='Chrome First Test')
        run_googlesearchdemo(wd, 'Chrome')

    def test_Safari(self):
        wd = load_webdriver_osx(browser='Safari', browser_version='13', session_name='Safari First Test')
        run_googlesearchdemo(wd, 'Safari')

    def test_Chrome_OSX(self):
        wd = load_webdriver_osx(browser='Chrome', browser_version='81', session_name='Chrome_OSX First Test')
        run_googlesearchdemo(wd, 'Chrome_OSX')
