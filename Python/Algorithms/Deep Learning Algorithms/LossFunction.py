"""
__FileCreationDate__  :  //2020
__Author__           :  coder-dev-geek
__Package__         :  Python 3
"""

import numpy as np


class SquareLoss(Loss):
    def __init__(self):
        pass

    def loss(self, y, y_pred):
        return 0.5 * ((y - y_pred) ** 2)

    def gradient(self, y, y_pred):
        return -(y - y_pred)

