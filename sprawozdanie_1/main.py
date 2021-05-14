import datetime
import time
from random import random, randrange

import sys

sys.setrecursionlimit(100000)
import matplotlib.pyplot as plt
import numpy as np

import algorithms
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


if __name__ == '__main__':
    algorithms_list = [
        # {
        #     "name": "Bubble Sort",
        #     "function_name": algorithms.bubble_sort
        # },
        # {
        #     "name": "Count Sort",
        #     "function_name": algorithms.count_sort
        # },
        # {
        #     "name": "Insertion Sort",
        #     "function_name": algorithms.insertion_sort
        # },
        # {
        #     "name": "Merge Sort",
        #     "function_name": algorithms.merge_sort
        # },
        # {
        #     "name": "Quick Sort",
        #     "function_name": algorithms.quickSort
        # },
        # {
        #     "name": "Shell Sort",
        #     "function_name": algorithms.shellSort
        # }
    ]

    for algorithm in algorithms_list:
        plt.xlabel("Number of elements")
        plt.ylabel("time [ms]")
        time_range = [*range(200,2500,100)]
        for data_gen_type in ["random",
                              "ascending",
                              "descending",
                              "constant",
                              "V-shaped",
                              "A-shaped"]:
            print("Type: ", data_gen_type)
            milis = []
            for point_quantities in range(200,2500,100):
                data = populate_data(data_gen_type, point_quantities)

                start = datetime.datetime.now()
                result = algorithm['function_name'](data,
                                                    # 0,
                                                    len(data)-1
                                                    )

                end = datetime.datetime.now()
                elapsed_time = end - start
                milliseconds = elapsed_time.microseconds/1000
                milis.append(milliseconds)



            print(milis)
            plt.plot(time_range, milis, label=data_gen_type)
        plt.legend()
        plt.title("Shell sort")
        plt.grid()
        plt.axis([0, 2500, 0, 20])
        plt.show()




                


                





