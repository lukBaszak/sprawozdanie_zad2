import collections


class Node(object):
    '''node'''

    def __init__(self, element):
        self.element = element

        self.next = None


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
            print(cur.element, end=' ')
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
        '''Delete node'''
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


if __name__ == '__main__':
    li = SingleLinkList()
    print('Is it empty?',li.is_empty())
    print('Is the length 0',li.length())
    li.append(1)
    print('Is it empty?',li.is_empty())
    print('Is the length 0',li.length())
    li.add(2)
    li.add(9)
    li.insert(1,10)
    li.travel()