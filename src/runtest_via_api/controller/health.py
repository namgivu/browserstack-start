import falcon
import json


class HealthController:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.body   = json.dumps({})
