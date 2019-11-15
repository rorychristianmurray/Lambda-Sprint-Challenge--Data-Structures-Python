from dll_stack_bst import Stack
from dll_queue_bst import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # set base case, initiate BST
        if self.value is None:
            self.value = value
            return

        if value < self.value:  # go left
            # check if we are at end of BST
            if not self.left:
                self.left = BinarySearchTree(value)
            else:  # keep moving but down the left side
                return self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:  # keep moving but down the right side
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:  # check for equality
            return True
        if target < self.value:  # look left
            if not self.left:  # if self.left is None (end)
                return False
            else:  # keep looking but down the left side
                return self.left.contains(target)
        else:
            if not self.right:  # if self.right is None (end)
                return False
            else:
                # keep looking but down the right side
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # check whether at end of list on right
        if self.right is None:
            return self.value
        else:  # recursively call on right
            return self.right.get_max()

        # solution II
        # return self.right.get_max() if self.right else self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    # this is a dft

    def for_each(self, cb):
        cb(self.value)
        if self.left:  # if self.left exists
            self.left.for_each(cb)
        if self.right:  # if self.right exists
            self.right.for_each(cb)

        # stack = []
        # stack.append(self)

        # [curr_node, r1, r2, r2, l1, l2, l3]

        # while len(stack):
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # create queue
        storage = Queue()
        # add root to queue
        storage.enqueue(node)
        while storage.len() > 0:
            currNode = storage.dequeue()
            print(currNode.value)
            if currNode.left:
                storage.enqueue(currNode.left)
            if currNode.right:
                storage.enqueue(currNode.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create stack
        storage = Stack()
        # add root to stack
        storage.push(node)
        while storage.len() > 0:
            currNode = storage.pop()
            print(currNode.value)
            if currNode.left:
                storage.push(currNode.left)
            if currNode.right:
                storage.push(currNode.right)

            # STRETCH Goals -------------------------
            # Note: Research may be required

            # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
