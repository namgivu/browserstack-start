import inspect


def obj_to_dict(obj):
    """ ref.https://stackoverflow.com/a/61522/248616 """
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            pr[name] = value
    return pr
