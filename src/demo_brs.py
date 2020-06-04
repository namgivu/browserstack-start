import time, os
from src.driver import windows_driver, osx_driver

APP_HOME = os.path.abspath(__file__ + '/../..')

def google_search(driver, browser_name):
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

class Test:

    def test_IE(self):
        dv = windows_driver(browser='IE', browser_version='11', name='IE First Test')
        google_search(dv, 'IE')

    def test_Edge(self):
        # TODO why can not run with Edge version 80 81
        dv = windows_driver(browser='Edge', browser_version='18', name='Edge First Test')
        google_search(dv, 'Edge')

    def test_Firefox(self):
        dv = windows_driver(browser='Firefox', browser_version='74', name='Firefox First Test')
        google_search(dv, 'Firefox')

    def test_Chrome(self):
        dv = windows_driver(browser='Chrome', browser_version='81', name='Chrome First Test')
        google_search(dv, 'Chrome')

    def test_Safari(self):
        dv = osx_driver(browser='Safari', browser_version='13', name='Safari First Test')
        google_search(dv, 'Safari')

    def test_Chrome_OSX(self):
        dv = osx_driver(browser='Chrome', browser_version='81', name='Chrome_OSX First Test')
        google_search(dv, 'Chrome_OSX')
