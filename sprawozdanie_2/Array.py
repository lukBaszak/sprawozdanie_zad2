import array as arr
from random import randrange
import datetime
import matplotlib.pyplot as plt
import sys

from main import populate_data

sys.setrecursionlimit(100000)

def f(value):
    return value


class Array:

    def __init__(self):
        self.arrayList = arr.array('i', [])

    def __len__(self):
        return len(self.arrayList)

    def insert(self, value):
        self.arrayList.append(value)

    def remove(self, value):

        i = len(self.arrayList) - 1
        while i >= 0:

            if self.arrayList[i] == value:
                del self.arrayList[i]
                break
            else:
                i-=1
    def contains(self, value):

        for i in range(0, len(self.arrayList) - 1):
            if self.arrayList[i] == value:
                return True
        return False

    def foreach(self):
        for i in range(0, len(self.arrayList) - 1):
            f(self.arrayList[i])


time_range = [*range(200,1000,100)]
fig, axs = plt.subplots(1, 2)
fig.suptitle('Array')


fig.text(0.5, 0.04, 'Number of elements', ha='center', va='center')
fig.text(0.04, 0.5, 'time [ms]', ha='center', va='center', rotation='vertical')



for data_gen_type in ["random",
                      "ascending",
                      "descending",
                      "constant",
                      "V-shaped",
                      "A-shaped"]:
    print("Type: ", data_gen_type)
    exists = []
    foreach = []
    for point_quantities in range(200,1000,100):
        data = populate_data(data_gen_type, point_quantities)
        arrTest = Array()

        for point in data:
            arrTest.insert(point)

        start = datetime.datetime.now()
        for point in data:
            arrTest.contains(point)
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        exists.append(milliseconds)

        start = datetime.datetime.now()
        for point in data:
            arrTest.foreach()
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        foreach.append(milliseconds)



    axs[0].plot(time_range, exists, label=data_gen_type)
    axs[0].set_title("Contains")
    axs[1].plot(time_range, foreach, label=data_gen_type)
    axs[1].set_title("ForEach")

    axs[0].axis([200, 1000, 0, 40])
    axs[1].axis([200, 1000, 0, 100])

plt.legend()
plt.show()
