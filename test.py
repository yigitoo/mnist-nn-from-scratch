"""
@author: Yiğit GÜMÜŞ <gh: yigitoo>
@title: The test module of this NeuralNetwork Model.
@Date: 27.01.2024 / @00.37
@version: v0.01
"""
from mnist import FirstModel

import random

model = FirstModel()
input_length = input('What numbers do you you want to test (default is random): ')
is_input_in_folder = input('Is the input in same folder (y/N): ').lower()

if (type(input_length) is str) and (input_length == ""):
    input_length: int = random.randint(0,9)

elif type(input_length) is int:
    if input_length >= 10: input_length: int = abs(input_length)
else:
    raise SystemExit("Failure: Invalid input length")

if is_input_in_folder == 'n':
    for _ in range(input_length):
        print('--------------------------------')
        model.run(input('Path of input: \n'))
        print()
else:
    input_folder = input('Path of input folder: ')
    #For example: C:/Users/johndoe/Documents/test_imgs/*.jpg
    #Or: /home/johndoe/Documents/test_imgs/*.jpg

    for i in range(1, input_length+1):
        print('--------------------------------\n')
        model.run(input_folder.replace('*', str(i)))
        print("")
