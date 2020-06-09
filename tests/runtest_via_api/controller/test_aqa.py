from falcon import testing
import json
from src.runtest_via_api.api import api


class Test(testing.TestCase):

    def setUp(self): self.app = api  # this field required by falcon.testing.TestCase; NOTE: Must declared here in setUp()


    def test(self):
        pass  #TODO


    def test_whenfailed(self):
        pass  # TODO


    def test_blank(self):
        INP = {
            'testcase_list': [
                'tests/test_blank.py::Test::test',  # follow syntax of pytest node id ref. https://docs.pytest.org/en/stable/usage.html#nodeids
            ],
        }
        self.simulate_post('/aqa', body=json.dumps(INP))
