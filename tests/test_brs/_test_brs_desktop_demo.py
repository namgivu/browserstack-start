from src.service.selenium_webdriver import load_webdriver_win10, load_webdriver_osx
from tests.test_brs.util import run_googlesearchdemo

class Test:
    """
    b   aka  browser_name
    v   aka  browser_version
    sn  aka  session_name
    wd  aka  webdriver
    """

    # mswindows
    def test_Chrome(self):     b='Chrome';    v='81'; sn='Chrome First Test'       ; wd=load_webdriver_win10(b, v, sn)   ; run_googlesearchdemo(wd, tag=f'{b}_win10')
    def test_Firefox(self):    b='Firefox';   v='74'; sn='Firefox First Test'      ; wd=load_webdriver_win10(b, v, sn)   ; run_googlesearchdemo(wd, tag=f'{b}_win10')
    def test_IE(self):         b='IE';        v='11'; sn='IE First Test'           ; wd=load_webdriver_win10(b, v, sn)   ; run_googlesearchdemo(wd, tag=f'{b}_win10')
    def test_Edge(self):       b='Edge';      v='18'; sn='Edge First Test'         ; wd=load_webdriver_win10(b, v, sn)   ; run_googlesearchdemo(wd, tag=f'{b}_win10')  # TODO why can not run with Edge version 80 81

    # macos
    def test_Chrome_OSX(self): b='Chrome';    v='81'; sn='Chrome_OSX First Test'   ; wd=load_webdriver_osx(b, v, sn)     ; run_googlesearchdemo(wd, tag=f'{b}_osx')
    def test_Safari(self):     b='Safari';    v='13'; sn='Safari First Test'       ; wd=load_webdriver_osx(b, v, sn)     ; run_googlesearchdemo(wd, tag=f'{b}_osx')
