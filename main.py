from torch.nn import Module
import torch

import pandas as pd
from sklearn.model_selection import train_test_split

from PIL import Image
import math

from typing import *
from classification import ( ResultVector, NumberVector )

""" Developing an MNIST model by scratch with NumPy an Mathematics. """

class FirstModel(Module):
    def __init__(self, version: str = 'v0.01',
                 author: str = 'Yiğit GÜMÜŞ'.encode('utf-8'),
                 nickname: str = 'FirstModel'):
        self.version = version
        self.author = author.decode('utf8') if (type(author) is bytes) else author
        self.nickname = nickname

        # For dataset and splitting it we are define these variables.
        self.dataset = None

        self.X_train = None
        self.y_train = None

        self.X_validation = None
        self.y_validation = None

        self.X_test = None
        self.y_test = None

    def __str__(self):
        return f"<{self.nickname}:{self.version} ; author: {self.author}>"

    def run(self, image: Image, predefined_result: int = None) -> ResultVector:
        #TODO: Implement here.
        result = ""

        print('Result: ')
        print(f'Label: {result}')
        print(f'Predefined result: {predefined_result}')
        image.show()
        return ResultVector.SUCCESS

    def test(self, image: Image=None) -> ResultVector:
        if type(image) is str:
            return self.run(Image.open(image))
        elif type(image) is Image:
               return self.run(image)
        else:
            print('The test image cannot be provided.')
            return ResultVector.FAILURE

    def load_dataset(self, target_variable: str, dataset: pd.DataFrame | str = None) -> ResultVector:
        if type(dataset) not in [pd.DataFrame, str]:
            print('No dataset provided.')
            return ResultVector.FAILURE
        if type(dataset) == str:
            dataset = pd.read_csv(dataset)

        [self.dataset, is_successful] = self.sampling_dataset(self.dataset)
        if is_successful:
            [(self.X_train, self.y_train),
            (self.X_validation, self.y_validation),
            (self.X_test, self.y_test),
            is_successful] = self.split_datasets(target_variable=target_variable,
                                                            train_percent=0.8,
                                                            test_percent=0.2)

            return ResultVector.SUCCESS if is_successful == True else ResultVector.FAILURE

    def sampling_dataset(self, dataset: pd.DataFrame) -> Tuple[Any, ResultVector]: #TODO: IMPLEMENT THIS FUNCTION!!
        condition = False #TODO: Implement this condition.

        if condition:
            print('Cannot sample dataset.')
            return (None, ResultVector.FAILURE)

        return (dataset, ResultVector.SUCCESS) #TODO: Implement here.

    def split_datasets(self, target_variable, train_percent: float, test_percent: float) -> Tuple[ #TODO: Implement validation set too.
        Tuple[Any, Any], Tuple[Any, Any], ResultVector
    ]:
        if self.dataset is None:
            print('Cannot split datasets because of no dataset provided.')
            return (
                None,
                None,
                None, ResultVector.FAILURE)
        elif math.fsum([train_percent, test_percent]) != 1.0:
            print('Please give the "train_percent" and "test_percent" certain values.\
                  \nCertain values: totals to be 1.0')
            return (
                None, None, None, ResultVector.FAIL
            )
        else:
            X_train, y_train, X_test, y_test = train_test_split(
                target = f'{target_variable}',
                train_size=train_percent,
                test_size=test_percent
            )

            return (
                (X_train, y_train),
                None #TODO: for now...
                (X_test, y_test),ResultVector.SUCCESS)

    def train(self) -> ResultVector:
        self.model = () # Boşdizi .D
        return ResultVector.SUCCESS #TODO: Implement here.

if __name__ == '__main__':
    try:
        from test import test
        test()
    except Exception as e:
        from pprint import pprint
        pprint(
            'Error: {e}\nArguments: {args}'.format(e=e, args=e.args))
