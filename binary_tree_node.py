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

    def bst_checker(self):
        """ Search tree
        :return:
        """
        # start at the root, with an arbitrarily low lower bound
        # and an arbitrarily high upper bound
        node_and_bounds_stack = [(self, -float('inf'), float('inf'))]

        # depth-first traversal
        while len(node_and_bounds_stack):
            node, lower_bound, upper_bound = node_and_bounds_stack.pop()

            # if this node is invalid, we return false right away
            if (node.value < lower_bound) or (node.value > upper_bound):
                return False

            if node.left:
                # this node must be less than the current node
                node_and_bounds_stack.append((node.left, lower_bound, node.value))
            if node.right:
                # this node must be greater than the current node
                node_and_bounds_stack.append((node.right, node.value, upper_bound))

        # if none of the nodes were invalid, return true
        # (at this point we have checked all nodes)
        return True

    def second_biggest(self):
        # Go through the tree in deep
        if not self.value:
            return None

        if not self.right and not self.left:
            return None
        second = self.value
        if not self.right and self.left:
            # The second biggest will be the biggest starting in the left branch
            ref_node = self.left
            consider_last_position = True
        else:
            # Left and right
            consider_last_position = False
            ref_node = self.right

        while ref_node.right:
            second = ref_node.value
            ref_node = ref_node.right

        if consider_last_position:
            return ref_node.value
        return second

n100 = BinaryTreeNode(100)
n90 = n100.insert_left(90)
n110 = n100.insert_right(110)
n8 = n90.insert_left(8)
n95 = n90.insert_right(95)
n115 = n110.insert_left(109)
n120 = n110.insert_right(120)
n7 = n120.insert_left(112)
n140 = n120.insert_right(140)


print n100.second_biggest()



class binary_node:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

class binary_tree:
	def __init__(self):
		self.root = None

	def __insert__(self, item):
		current_node = self.root
		while current_node.next:
			if (item > current_node.value):
				current.node = current.node.self.rightChild
			else:
				current.node = current.node.self.leftChild


#
#
# def build_tree(sorted_array, node, low, high):
# 	if (low == high):
# 		return parent_node
# 	else:
# 		# find the middle element
# 		El = sorted_array[int((high+low)/2)]
# 		# insert the middle element at the root
# 		node.value = 	sorted_array[El]
# 		node.leftChild= binary_node()
# 		node.rightChild= binary_node()
# 		build_tree(sorted_array, Node.leftChild, 0, El)
# 		build_tree(sorted_array, Node.rightChild, El, high)