import datetime
import time
from random import random, randrange

import sys

sys.setrecursionlimit(100000)
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

def populate_data(datatype, limit):
    data = []

    for i in range(0, limit):

        if datatype == "random":
            data.append(randrange(100))
        if datatype == "ascending":
            data.append(i * 2)
        if datatype == "descending":
            data.append((limit - i) * 2)
        if datatype == "constant":
            data.append(100)
        if datatype == "V-shaped":
            if limit/2 >= i:
                data.append((limit - i) * 2)
            else:
                data.append(i * 2)
        if datatype == "A-shaped":
            if limit/2 >= i:
                data.append((limit - i) * 2)
            else:
                data.append(i * 2)

    return data



                


                





