import torch.nn as nn

import torch

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 3, 3)
        self.relu1 = nn.ReLU()
        self.mp1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(3, 3, 3)
        self.relu2 = nn.ReLU()
        self.mp2 = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(108, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 10)
    def forward(self, x):
        out = self.conv1(x)
        out = self.relu1(out)
        out = self.mp1(out)
        out = self.conv2(out)
        out = self.relu2(out)
        out = self.mp2(out)
        out = self.flatten(out)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out

if __name__ == "__main__":
    model = Model()
    x = torch.ones((64, 3, 32, 32))
    print(model.forward(x))
