from falcon import testing
import json
from src.runtest_via_api.api import api


class Test(testing.TestCase):

    def setUp(self): self.app = api  # this field required by falcon.testing.TestCase; NOTE: Must declared here in setUp()


    def test_blank(self):
        INP={ 'testcase_list': [ 'tests/test_blank.py::Test::test'] }  # follow syntax of pytest node id ref. https://docs.pytest.org/en/stable/usage.html#nodeids
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code == 200


    def test_failonpurpose(self):
        INP={ 'testcase_list': [ 'tests/_test_failonpurpose.py::Test::test'] }  # follow syntax of pytest node id ref. https://docs.pytest.org/en/stable/usage.html#nodeids
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code != 200


    def test_brs_mobile(self):
        INP={ 'testcase_list': [
            'tests/test_brs/_test_brs_mobile_demo.py::Test::test_android',
            'tests/test_brs/_test_brs_mobile_demo.py::Test::test_ios',
        ] }
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code == 200


    def test_brs_desktop(self):
        INP={ 'testcase_list': [
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_Chrome',
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_Firefox',
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_IE',
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_Edge',
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_Chrome_OSX',
            'tests/test_brs/_test_brs_desktop_demo.py::Test::test_Safari',
        ] }
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code == 200
