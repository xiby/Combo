import torch
import torchvision

from util import LogUtil
from torchvision import datasets
from model.Model import Model
from LearningAgent import LearningAgent
from util.NetworkUtil import NetworkUtil

logger = LogUtil.getLogger(__file__)
if __name__ == "__main__":
    logger.info("start main")
    fullDataset = datasets.CIFAR10(
        root="../data",
        train=True,
        download=True,
        transform=torchvision.transforms.ToTensor()
    )
    data,label = fullDataset[0]
    logger.info(data.shape)
    model = Model()
    agent = LearningAgent(0, model, None, None, None, None)
    T = agent.flatten()
    logger.info(T.shape)
    param=agent.recoverModel(T)
    logger.info("test finished")
    util1 = NetworkUtil()
    util2 = NetworkUtil()
    logger.info(util1 == util2)