from random import randrange
import datetime
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)


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

def f(i):
    return i

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def foreach(self):
        if self.left:
            self.left.foreach()
        f(self.val)
        if self.right:
            self.right.foreach()

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals



time_range = [*range(200,3000,500)]
fig, axs = plt.subplots(1, 2)
fig.suptitle('BST')


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
    for point_quantities in range(200,3000,500):
        data = populate_data(data_gen_type, point_quantities)
        bst = BSTNode()



        start = datetime.datetime.now()
        for point in data:
            bst.insert(point)
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        exists.append(milliseconds)

        start = datetime.datetime.now()
        for point in data:
            bst.delete(point)
        end = datetime.datetime.now()

        elapsed_time = end - start
        milliseconds = elapsed_time.microseconds/1000
        foreach.append(milliseconds)



    axs[0].plot(time_range, exists, label=data_gen_type)
    axs[0].set_title("Contains")
    axs[1].plot(time_range, foreach, label=data_gen_type)
    axs[1].set_title("ForEach")

    axs[0].axis([200, 3000, 0, 1000])
    axs[1].axis([200, 3000, 0, 1000])

plt.legend()
plt.show()