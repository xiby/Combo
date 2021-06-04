import torch

from collections import OrderedDict
from util import LogUtil

logger = LogUtil.getLogger(__file__)
class LearningAgent():
    def __init__(self, id, segment_id, segment_size, model, loss_fn, optimizor, train_dataloader, test_dataloader):
        super().__init__()
        self.id = id
        self.segment_id = segment_id
        self.segment_size = segment_size
        self.model = model
        self.loss_fn = loss_fn
        self.optimizor = optimizor
        self.train_dataloader = train_dataloader
        self.test_dataloader = test_dataloader
        self.param = model.state_dict()
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)
        self.size = len(self.train_dataloader.dataset)
    def flatten(self):
        '''
        flattern the param
        '''
        ret = None
        for key in self.param.keys():
            if ret is None:
                ret = torch.flatten(self.param[key])
            else:
                ret = torch.cat((ret, torch.flatten(self.param[key])))
        return ret
    
    def recoverModel(self, T):
        '''
        translate the flattened param to model
        '''
        index = 0
        trueParam = OrderedDict()
        for key in self.param.keys():
            sp = self.param[key].shape
            total = 1
            for item in sp:
                total *= item
            target_index = index + total
            sub_tensor = T[index:target_index]
            trueParam[key] = torch.reshape(sub_tensor, sp)
            index = target_index
        return trueParam

    def train_model(self, epoch):
        '''
        train the model
        '''
        size = len(self.train_dataloader.dataset)
        for i in range(epoch):
            for batch, (X, y) in enumerate(self.train_dataloader):
                X, y = X.to(self.device), y.to(self.device)
                pred = self.model(X)
                loss = self.loss_fn(pred, y)
                self.optimizor.zero_grad()
                loss.backward()
                self.optimizor.step()
                loss, current = loss.item, (batch + 1) * len(X)
                logger.info(f"client: {self.id} epoch: {i} loss: {loss:>7f} [{current:>5d}/{size:>5d}]")

    def test_model(self):
        '''
        test the model
        '''
        size = len(self.test_dataloader.dataset)
        test_loss, correct = 0, 0
        with torch.no_grad():
            for X, y in self.test_dataloader:
                X, y = X.to(self.device), y.to(self.device)
                pred = self.model(X)
                test_loss += self.loss_fn(pred, y).item()
                correct += (pred.argmax(1) == y).type(torch.float).sum().item()
        test_loss /= size
        correct /= size
        logger.info(f"Client: {self.id}, Acc: {(100*correct):0.5f}%, avg loss: {test_loss:>8f}")

    def aggregation(self):
        '''
        TODO implement it
        '''
        pass
    def report_segment(self, segmentSize, segment_id):
        '''
        return a dict
        '''
        T = self.flatten()
        start = segment_id * self.segment_size,
        end = start + self.segment_size
        seg = T[start:end]
        return {'id': self.id, 'segment_id': self.segment_id, 'seg': seg, 'size': self.size}
    def receive(self, source, body):
        self.received[source] = body
