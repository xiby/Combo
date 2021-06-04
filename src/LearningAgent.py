import torch

from collections import OrderedDict
class LearningAgent():
    def __init__(self, id, model, loss_fn, optimizor, train_dataloader, test_dataloader):
        super().__init__()
        self.id = id
        self.model = model
        self.loss_fn = loss_fn
        self.optimizor = optimizor
        self.train_dataloader = train_dataloader
        self.test_dataloader = test_dataloader
        self.param = model.state_dict()
    def flatten(self):
        '''
        flattern the param
        '''
        ret = None
        for key in self.param.keys():
            if ret is None:
                ret = torch.flatten(self.param[key])
            else:
                ret = torch.cat(ret, torch.flatten(self.param[key]))
        return ret
    
    def recoverModel(self, T):
        '''
        translate the flattened param to model
        '''
        index = 0
        trueParam = OrderedDict()
        for key in self.keys():
            m,n,h,w = self.param[key].shape
            target_index = index + m*n*h*w
            sub_tensor = T[index:target_index]
            trueParam[key] = torch.reshape(sub_tensor, (m,n,h,w))
            index = target_index

