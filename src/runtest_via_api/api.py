import falcon

from src.runtest_via_api.controller.health  import HealthController
from src.runtest_via_api.controller.aqa     import AQAController


api = falcon.API()

#              route        controller
api.add_route('/health',    HealthController() )
api.add_route('/aqa',       AQAController() )
