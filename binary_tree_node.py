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

    def is_search_tree(self):
        # Base cases (single node)
        if self.left is None and self.right is None:
            return True

        if self.value is None:
            print "Found Null node!"
            return False

        # Analyze first two child nodes
        if self.left is not None:
            if self.left.value >= self.value:
                print("Broken left rule. Child value:{0}; Parent value:{1}".format(self.left.value, self.value))
                return False
        if self.right is not None:
            if self.right.value <= self.value:
                print("Broken right rule. Child value:{0}; Parent value:{1}".format(self.right.value, self.value))
                return False

        # Traverse the tree in breadth-first. For every node we save the parent value as max and min
        nodes = [(self.left, self.value), (self.right, self.value)]
        while len(nodes) > 0:
            node_tuple = nodes.pop(0)
            node = node_tuple[0]
            if node is None:
                continue
            if node.value is None:
                print "Found Null node!"
                return False
            print("Analyzing node {0}".format(node.value))
            print(nodes)

            if node.left is not None:
                # Check if the value of the left node is not smaller than the parent
                if node.left.value >= node.value:
                    print("Broken left rule. Child value:{0}; Parent value:{1}".format(node.left.value, node.value))
                    return False
                if node_tuple[1] is not None and node.left.value <= node_tuple[1]:
                    print("Broken rule. Node {0} is smaller than the minimum value ({1})".format(node.left.value, node_tuple[1]))
                    return False
                # Insert the new node to be analyzed. We just need to keep track of the new minimum for right nodes
            nodes.append((node.left, node.value))

            if node.right is not None:
                # Check if the value of the left node is not smaller than the parent
                if node.right.value <= node.value:
                    print("Broken right rule. Child value:{0}; Parent value:{1}".format(node.right.value, node.value))
                    return False
                if node_tuple[1] is not None and node.right.value >= node_tuple[1]:
                    print("Broken rule. Node {0} is bigger than the maximum value ({1})".format(node.right.value, node_tuple[1]))
                    return False
                # Insert the new node to be analyzed. We just need to keep track of the new maximum for left nodes
            nodes.append((node.right, node.value))
        return True

    def __str__(self):
        if self.value is None: return "None"
        return str(self.value)
           



        #
        #
        # nodes = [(self.left, self.value, self.value), (self.right, self.value, self.value)]
        # while len(nodes) > 0:
        #     node_left = nodes.pop(0)
        #     node_right = nodes.pop(0)
        #     if node_left[0] is not None:
        #         print("Left: {0}; ({1},{2})".format(node_left[0].value, node_left[1], node_left[2]))
        #     else:
        #         print("None")
        #     if node_right[0] is not None:
        #         print("Right: {0}; ({1},{2})".format(node_right[0].value, node_right[1], node_right[2]))
        #     else:
        #         print("None")
        #     # print("Left: {0}, Right: {1}".format(node_left[0].value if node_left[0] is not None else "None",
        #     #                                      node_right[0].value if node_right[0] is not None else "None"))
        #
        #     if node_left[0] is not None:
        #         # Check the value of the left child is smaller than the parent
        #         if node_left[0].value >= node_left[1] or node_left[0].value >= node_left[2]:
        #             # Break the rule!
        #             print("Broken left rule: {0}; {1}; {2}".format(node_left[0].value, node_left[1], node_left[2]))
        #             return False
        #         # Set a new minimum, but keep the same maximum
        #         nodes.append((node_left[0].left, node_left[0].value, node_left[2]))
        #         nodes.append((node_left[0].right, node_left[0].value, node_left[2]))
        #     if node_right[0] is not None:
        #         if node_right[0].value <= node_right[1] or node_right[0].value <= node_right[2]:
        #             # Break the rule!
        #             print("Broken right rule: {0};{1};{2}".format(node_right[0].value, node_right[1], node_right[2]))
        #             return False
        #         nodes.append((node_right[0].left, node_right[0].value, node_right[2]))
        #         nodes.append((node_right[0].right, node_right[0].value, node_right[2]))
        #     #print nodes
        # return True




n100 = BinaryTreeNode(100)
n90 = n100.insert_left(90)
n110 = n100.insert_right(110)
n8 = n90.insert_left(8)
n95 = n90.insert_right(95)
n115 = n110.insert_left(75)
n120 = n110.insert_right(120)
n7 = n120.insert_left(112)
n140 = n120.insert_right(140)


print n100.is_search_tree()