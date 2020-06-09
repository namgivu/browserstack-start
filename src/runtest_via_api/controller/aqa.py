import falcon
import json
import os

from textwrap import dedent


CODE_HOME = os.path.abspath(os.path.dirname(__file__))
APP_HOME  = os.path.abspath(f'{CODE_HOME}/../../..')


class AQAController:

    def on_post(self, req, resp):
        jb = req.media  # jb aka json_body
        tc_all = jb.get('testcase_list')  # tc_all aka testcase_all
        for tc in tc_all:
            sp=tc.split('::')
            tc_file   = sp[0]
            tc_class  = sp[1] if 1<len(sp) else None
            tc_method = sp[2] if 2<len(sp) else None

            #region runtime executing code at file :tc

            # load :tc_file into a python module ref. https://stackoverflow.com/a/54956419/248616
            import importlib.util
            f=f'{APP_HOME}/{tc_file}'
            module_name = 'some_module_name'  #TODO can this be the filename of :f
            spec        = importlib.util.spec_from_file_location(module_name, f)
            module      = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            #TODO handle when tc_class is None ie running all TestXXX classes
            #TODO handle when tc_method is None ie running all :tc_class.test_xxx() methods

            # create instance :o from class name as :tc_class ref. https://stackoverflow.com/a/4821120/248616
            k = getattr(module, tc_class)  # k aka klass ie class_
            o = k()

            # run test method of :o with method name as :tc_method ref. https://stackoverflow.com/a/3071/248616
            m = getattr(o, tc_method)
            m()
            #endregion runtime executing code at file :tc

        resp.status = falcon.HTTP_OK
        resp.body   = json.dumps({})
