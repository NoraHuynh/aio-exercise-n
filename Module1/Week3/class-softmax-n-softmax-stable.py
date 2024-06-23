import torch
import torch.nn as nn
import math


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        n = len(x)
        sum_e = sum([math.exp(x[j]) for j in range(n)])
        sftmax = torch.Tensor([math.exp(x[i]) / sum_e for i in range(n)])
        return sftmax


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
