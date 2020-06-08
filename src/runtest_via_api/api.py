import falcon
from src.runtest_via_api.controller.health import HealthController


api = falcon.API()
api.add_route('/health', HealthController() )
