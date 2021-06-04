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
        self.content = dict()
    def set_content(self, key, value, replace = True):
        if key in self.content.keys() and not replace:
            return
        else:
            self.content[key] = value
    def set_clients(self, clients):
        self.content['clients'] = clients
    def set_segments(self, segments, segment_size):
        self.content['segments'] = segments
        self.content['segment_size'] = segment_size
    def request(self, target, segment_id):
        return self.content['clients'][target].report_segment(self.content['segment_size'], segment_id)
    def send(self, target, body):
        self.content['clients'][target].receive(target, body)