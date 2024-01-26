import pandas as pd
import numpy as np

import PIL
from PIL import Image

from typing import *
from classification import ( ResultVector, Numbers )

rv = ResultVector

""" Developing an MNIST model by scratch with NumPy an Mathematics. """

class FirstModel(object):
    def __init__(self, version: str = 'v0.01',
                 author : str = 'Yiğit GÜMÜŞ'.encode('utf-8'),
                 nickname: str = 'FirstModel'):
        self.version = version
        self.author = author.decode('utf8') if (type(author) is bytes) else author
        self.nickname = nickname

    def __str__(self):
        return f"<{self.nickname}:{self.version} ; author: {self.author}>"

    def run(self, image: Image, predefined_result: int = None) -> ResultVector:
        #TODO: Implement here.
        result = ""

        print('Result: ')
        print(f'Label: {result}')
        print(f'Predefined result: {predefined_result}')
        image.show()
        return rv.SUCCESS

    def test(self, image: Image=None) -> ResultVector:
        if type(image) is str:
            return self.run(Image.open(image))
        elif type(image) is Image:
            return self.run(image)
        else:
            print('The test image cannot be provided.')
            return rv.FAILURE

    def load_dataset(self, dataset: pd.DataFrame=None) -> ResultVector:
        if dataset == None:
            print('No dataset provided.')
            return rv.FAILURE
        else:
            self.dataset = self.sampling_dataset(dataset)
            return rv.SUCCESS

    def sampling_dataset(self, dataset: pd.DataFrame) -> ResultVector: pass #TODO: Implement here.

    def split_datasets(self) -> ResultVector:
        if self.dataset is None:
            print('Cannot split datasets because of no dataset provided.')
            return rv.FAILURE
        else:
            pass #TODO: Implement here.
            return rv.SUCCESS

    def test_dataset(self, dataset: pd.DataFrame): pass #TODO: Implement here.

    def process() -> ResultVector: pass #TODO: Implement here.

    def train() -> ResultVector: pass #TODO: Implement here.

if __name__ == '__main__':
    model = FirstModel()
    try:
        FirstModel.test('test/0.jpg')
    except Exception as e:
        __import__('pprint').pprint(
            'Error: {e}\nArguments: {args}'.format(e=e, args=e.args))
