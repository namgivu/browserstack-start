import time, os
from src.driver import load_webdriver_mswindows, load_webdriver_macos

APP_HOME = os.path.abspath(__file__ + '/../..')

def run_googlesearchdemo(driver, browser_name):
    driver.get('http://www.google.com')

    # enter search keyword
    search_input = driver.find_element_by_name('q')
    search_input.send_keys('360f product')
    search_input.submit()

    # take screenshot
    time.sleep(3)
    driver.save_screenshot(f'{APP_HOME}/screen_shot/{browser_name}.png')

    # the end
    driver.quit()  # CAUTION: don't forget to call .quit() or you will get timeout from :brs


#TODO Trang what is param :name for in > dv = windows_driver(browser='IE', browser_version='11', name='IE First Test')
class Test:

    def test_IE(self):
        dv = load_webdriver_mswindows(browser='IE', browser_version='11', name='IE First Test')
        run_googlesearchdemo(dv, 'IE')

    def test_Edge(self):
        # TODO why can not run with Edge version 80 81
        dv = load_webdriver_mswindows(browser='Edge', browser_version='18', name='Edge First Test')
        run_googlesearchdemo(dv, 'Edge')

    def test_Firefox(self):
        dv = load_webdriver_mswindows(browser='Firefox', browser_version='74', name='Firefox First Test')
        run_googlesearchdemo(dv, 'Firefox')

    def test_Chrome(self):
        dv = load_webdriver_mswindows(browser='Chrome', browser_version='81', name='Chrome First Test')
        run_googlesearchdemo(dv, 'Chrome')

    def test_Safari(self):
        dv = load_webdriver_macos(browser='Safari', browser_version='13', name='Safari First Test')
        run_googlesearchdemo(dv, 'Safari')

    def test_Chrome_OSX(self):
        dv = load_webdriver_macos(browser='Chrome', browser_version='81', name='Chrome_OSX First Test')
        run_googlesearchdemo(dv, 'Chrome_OSX')
