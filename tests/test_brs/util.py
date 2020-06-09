import time, os

APP_HOME = os.path.abspath(__file__ + '/../../..')

def run_googlesearchdemo(wd: 'web driver', tag: 'run tag used in snapshot filename'):  #TODO remove browser_name   #TODO should we name :driver as :wd ie :webdriver?
    wd.get('http://www.google.com')

    # enter search keyword
    search_input = wd.find_element_by_name('q')
    search_input.send_keys('360f product')
    search_input.submit()

    # take screenshot
    time.sleep(3)
    wd.save_screenshot(f'{APP_HOME}/screen_shot/{tag}.png')

    # the end
    wd.quit()  # CAUTION: don't forget to call .quit() or you will get timeout from :brs
