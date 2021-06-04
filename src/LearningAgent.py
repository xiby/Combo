import torch
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
    def flattern(self):
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

