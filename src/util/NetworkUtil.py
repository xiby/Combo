'''
net work util, for sending msg
'''
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class NetworkUtil():
    def __init__(self):
        '''
        do nothing
        '''