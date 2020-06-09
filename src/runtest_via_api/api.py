import os
import traceback

import falcon
from falcon_cors import CORS
import json

from src.service.misc import obj_to_dict
from src.runtest_via_api.controller.health  import HealthController
from src.runtest_via_api.controller.aqa     import AQAController


#region middleware
''' allow all cors origins+methods ref. https://stackoverflow.com/a/60036107/248616 '''
cors = CORS(
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True,
)

middleware = [
    cors.middleware,  # cors config ref. https://github.com/lwcolton/falcon-cors#usage
]
#endregion middleware


api = falcon.API(middleware=middleware)


#region customize exception response
def generic_error_handler(ex, req, resp, params):  # ex aka exception, req aka request, resp aka response
    """
    custom exception response ref. https://stackoverflow.com/a/52464930/248616
    CAUTION this will gobble actual HTTPError returned from the application code ref. https://stackoverflow.com/a/60606760/248616
    """
    r = {}  # r aka json_result

    #region print :ex to json
    #TODO may need more elegant way to print :ex to json string/object; currently with ex=HTTPNotFound, keeping raw :ex we get error > TypeError: Object of type 'HTTPNotFound' is not JSON serializable
    ex_d = obj_to_dict(ex)  # ex_d aka ex_to_dict
    s = None
    if not s: s = ex_d.get('message')
    if not s: s = ex_d.get('title')
    if not s:
        if str(ex):
            s = f'ERROR:{str(ex)} - TYPE:{type(ex)}'
    if not s: raise Exception('Cannot convert exception :ex to string')
    r['exception'] = s

    r['stacktrace']={}
    r['stacktrace']['stacktrace1 traceback.format_exc()'] = traceback.format_exc()  #TODO This not print the full stacktrace ie only trace in .venv and not in our api code
    #r['stacktrace']['stacktrace2 sys.exc_info()[2]'] = sys.exc_info()[2]  # ref. https://stackoverflow.com/a/3702847/248616  #TODO consider to combine this trace
    #r['stacktrace']['stacktrace3 traceback.format_exception(sys.exc_info())'] = traceback.format_exception(sys.exc_info())   #TODO consider to combine this trace

    if params: r['params'] = params

    r['request'] = str(req)

    #endregion print :ex to json

    # conclusion result
    r = {
        'error'      : True,
        'description': r,
    }

    #region add :errorCode if any
    '''
    errorCode appears as prefix to r['exception']
    > errorCode=VPR0081 Exception: Cannot get mortality rate for anb=18, gender=M, smoker=N, term=5
    '''
    try:    errorText = ex_d.get('args')[0]
    except: errorText = ''

    try:    errorCode = ex_d.get('args')[1] if 'errorCode=' in errorText else ''
    except: errorCode = None
    if errorCode: r['errorCode'] = errorCode
    #endregion

    resp.status = falcon.HTTP_400
    resp.body = json.dumps(r)

SKIP_ERROR_HANDLER = os.environ.get('SKIP_ERROR_HANDLER') ; ADD_ERROR_HANDLER  = 1 if SKIP_ERROR_HANDLER is None or SKIP_ERROR_HANDLER=='0' else 0  # this is negative of SKIP_ERROR_HANDLER
if ADD_ERROR_HANDLER: api.add_error_handler(Exception, generic_error_handler)  # NOTE: recommended to set SKIP_ERROR_HANDLER=1 to when fixing unittest to see the normal/popular error printed in PyCharm
#endregion customize exception response


#              route        controller
api.add_route('/health',    HealthController() )
api.add_route('/aqa',       AQAController() )
