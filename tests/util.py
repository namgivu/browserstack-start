import time, os

APP_HOME = os.path.abspath(__file__ + '/../..')

def run_googlesearchdemo(driver, browser_name):  #TODO remove browser_name   #TODO should we name :driver as :wd ie :webdriver?
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
