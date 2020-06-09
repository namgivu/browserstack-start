from falcon import testing
import json
from src.runtest_via_api.api import api


class Test(testing.TestCase):

    def setUp(self): self.app = api  # this field required by falcon.testing.TestCase; NOTE: Must declared here in setUp()


    def test(self):
        pass  #TODO


    def test_blank(self):
        INP={ 'testcase_list': [ 'tests/test_blank.py::Test::test'] }  # follow syntax of pytest node id ref. https://docs.pytest.org/en/stable/usage.html#nodeids
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code == 200


    def test_failonpurpose(self):
        INP={ 'testcase_list': [ 'tests/_test_failonpurpose.py::Test::test'] }  # follow syntax of pytest node id ref. https://docs.pytest.org/en/stable/usage.html#nodeids
        r = self.simulate_post('/aqa', body=json.dumps(INP))
        assert r.status_code != 200
