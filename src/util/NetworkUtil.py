'''
net work util, for sending msg
'''
import random

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
        init content
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
    def pull(self, select_size):
        '''
        pull the full segment
        return a list  [[{},{},{}]: segment 1, [{},{},{}]: segment 2 ]
        we assume that each client is idea, and we select clients randomly
        '''
        segments = self.content['segments']
        ret = []
        for segment_id in range(len(segments)):
            '''
            random select some clients from one segment
            '''
            ret_item = []
            indices = random.sample(range(len(segments[segment_id])), select_size)
            for index in indices:
                report = self.content['clients'][index].report_segment(self.content['segment_size'], segment_id)
                ret_item.append(report)
            ret.append(ret_item)
        return ret

    def _request(self, target, segment_id):
        return self.content['clients'][target].report_segment(self.content['segment_size'], segment_id)
    def send(self, target, body):
        self.content['clients'][target].receive(target, body)