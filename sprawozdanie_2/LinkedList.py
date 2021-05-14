from main import populate_data

import datetime
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)


class Node(object):
    '''node'''

    def __init__(self, element):

        self.element = element
        self.next = None


def f(element):
    return element


class SingleLinkList(object):
    '''Realize single chain table and connect nodes in series'''

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        '''Judge whether the list is empty'''

        return self.__head == None

    def length(self):
        '''Return the length of the linked list'''


        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''Traverse the entire list'''
        cur = self.__head
        while cur != None:
            f(cur.element)
            cur = cur.next

    def add(self, item):
        '''Add elements to the head'''


        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''Add elements at the end of the list,Tail insertion method'''

        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''Insert element at specified location'''

        if pos <= 0:
            self.add(item)

        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0

            while count < (pos - 1):
                pre = pre.next
                count += 1

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.__head is None:
            return
        if self.__head.element == item:
            self.__head = self.__head.next
        else:
            previous = self.__head
            current = self.__head.next

            while current is not None:
                if current.element == item:
                    previous.next = current.next
                    break

                previous = current
                current =current.next
        pass

    def search(self, item):
        '''Find whether the node exists'''
        cur = self.__head
        while cur != Node:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        return False



time_range = [*range(200,1000,100)]
fig, axs = plt.subplots(1, 2)
fig.suptitle('One-way list')


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
        sl = SingleLinkList()



        start = datetime.datetime.now()
        for point in data:
            sl.append(point)
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        exists.append(milliseconds)

        start = datetime.datetime.now()
        for point in data:
            sl.remove(point)
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        foreach.append(milliseconds)



    print(foreach)
    axs[0].plot(time_range, exists, label=data_gen_type)
    axs[0].set_title("Insert")
    axs[1].plot(time_range, foreach, label=data_gen_type)
    axs[1].set_title("Remove")

    axs[0].axis([200, 1000, 0, 250])
    axs[1].axis([200, 1000, 0, 2])

plt.legend()
plt.show()
