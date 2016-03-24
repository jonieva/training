class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_superbalanced(self):
        """ A n1 is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.
        :return: Bool
        """
        # Check base cases
        if self.left is None and self.right is None:
            return True

        # if self.left is None and self.right is not None or \
        #     self.right is None and self.left is not None:
        #     return False

        last_depth = None
        depth = 1
        # go over the n1 in depth. Stop if I find a leaf node with a depth different to the last stored
        nodes = [(self.right, 1), (self.left,1)]
        while len(nodes) > 0:
            # Get first node
            elem = nodes.pop()
            current = elem[0]
            depth = elem[1]

            if current is not None:
                print ("Node: {0}; Depth: {1};".format(current.value, depth))
                if current.is_leaf():
                    if last_depth is None:
                        # First leaf node
                        last_depth = depth
                    elif depth != last_depth:
                        # We found a leaf node with a different depth. There's no need to go on
                        print ("found leaf with depth {0}!={1}".format(depth, last_depth))
                        return False
                else:
                    # Add the next nodes to be visited later (append them to the beginning of the list)
                    nodes.append((current.right, depth + 1))
                    nodes.append((current.left, depth + 1))
            else:
                print("Current node: None. Depth: ", depth )
        # If we went over the whole n1, it is balanced
        return True

    def is_leaf(self):
        if self is None:
            return False
        return self.left is None and self.right is None


n1 = BinaryTreeNode(1)
n2 = n1.insert_left(2)
n7 = n1.insert_right(7)
n3 = n2.insert_left(3)
n4 = n3.insert_right(4)
n5 = n2.insert_right(5)
n6 = n5.insert_left(6)
n8 = n7.insert_right(8)
n9 = n8.insert_left(9)
n10 = n8.insert_right(10)
n11 = n10.insert_left(11)

print n1.is_superbalanced()