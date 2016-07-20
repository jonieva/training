# import numpy as np
#
#
# class binary_node:
#     def __init__(self, value):
#         self.value = value
#         self.leftChild = None
#         self.rightChild = None
#
#     def node_inorder(self):
#         if self.leftChild:
#             self.leftChild.node_inorder()
#         print(self.value)
#         if self.rightChild:
#             self.rightChild.node_inorder()
#
#     def pprint(self):
#         s = "[" + str(self.value)
#         if self.leftChild:
#             s += self.leftChild.pprint()
#         else:
#             s += "[]"
#
#         if self.rightChild:
#             s += self.rightChild.pprint()
#         else:
#             s += "[]"
#         s += "]"
#         return s
#
#
# class binary_tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, item):
#         if self.root is None:
#             self.root = binary_node(item)
#         else:
#             current_node = self.root
#
#             while ((current_node.leftChild) and (item < current_node.value)) or \
#                     ((current_node.rightChild) and (item > current_node.value)):
#                 if (item > current_node.value):
#                     current_node = current_node.rightChild
#                 else:
#                     current_node = current_node.leftChild
#
#             if (item > current_node.value):
#                 current_node.rightChild = binary_node(item)
#             else:
#                 current_node.leftChild = binary_node(item)
#
#     def build_recursive_(self, sorted_array, low, high):
#         """ build a tree usign a subset of an array starting with the parent node"""
#         """ return the root node"""
#         middle_element = int((high + low) / 2)
#
#         # print(str(low)+str(high)+str(middle_element))
#
#         if (high >= low):
#             self.insert(sorted_array[middle_element])
#
#         if (high <= low):
#             return
#         else:
#             # insert the middle element at the root
#             self.build_recursive_(sorted_array, low, middle_element - 1)
#             self.build_recursive_(sorted_array, middle_element + 1, high)
#
#     def build_tree_recursive(self, input_array):
#         self.build_recursive_(input_array, 0, np.shape(input_array)[0] - 1)
#
#         return self.root
#
#     def inorder(self):
#         self.root.node_inorder()
#
#     def build_tree_unrecursive(self, input_array):
#         num_elements = np.shape(input_array)[0]
#
#         assert num_elements > 0, "must have at least 1 element to build tree"
#         if (num_elements == 1):
#             self.insert(input_array[0])
#             return
#         # We need to place N elements in the array
#         # We need to go through them in the order that they should be
#         # presented in the tree
#
#         # populate the levels 1 by 1
#         num_levels = int(np.log2(num_elements)) + 1
#         current_indices = [0, num_elements - 1]
#         for level_index in range(0, num_levels):
#             next_indices = []
#             for array_index in range(0, (np.shape(current_indices)[0] - 1)):
#                 # keep it for next time
#                 current_array_index = current_indices[array_index]
#
#                 next_indices.append(current_array_index)
#                 next_index_array = int((current_array_index + current_indices[array_index + 1]) / 2)
#                 # if it is a valid array index, then insert and append index for next time
#                 if ((next_index_array < num_elements) and (
#                             (current_array_index + 1) < current_indices[array_index + 1])):
#                     self.insert(input_array[next_index_array])
#                     next_indices.append(next_index_array)
#
#             # append the last index
#             next_indices.append(current_indices[np.shape(current_indices)[0] - 1])
#             current_indices = next_indices
#
#         # insert first and last element
#         self.insert(input_array[0])
#         self.insert(input_array[-1])


class binaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def create_binary_tree(sorted_array):
    l = len(sorted_array)
    if l == 0:
        return None
    if l == 1:
        return binaryNode(sorted_array[0])
    pending = []

    root_pos = l / 2
    root_node = binaryNode(sorted_array[root_pos])
    LEFT = 0
    RIGHT = 1
    # Create tuples of (root_node, side(left-right), start_pos, end_pos)
    pending.append((root_node, LEFT, 0, root_pos - 1))
    pending.append((root_node, RIGHT, root_pos + 1, l - 1))

    # Iterate to extract left branches
    while len(pending) > 0:
        t = pending.pop(0)
        root_pos = (t[3] - t[2]) / 2 + t[2]
        # Create the node
        node = binaryNode(sorted_array[root_pos])
        # Link the current node with the previous parent node
        # The node will be the left or child of the parent node (t[0])
        if t[1] == LEFT:
            t[0].left = node
        else:
            t[0].right = node
        # Process left branch
        if t[2] == root_pos - 1:
            # End of left branch. Insert a node directly
            node.left = binaryNode(sorted_array[t[2]])
        elif t[2] < root_pos - 1:
            # We still have to loop
            pending.append((node, LEFT, t[2], root_pos - 1))
        # Process right branch
        if t[3] == root_pos + 1:
            # End of right branch. Insert a node directly
            node.right = binaryNode(sorted_array[t[3]])
        elif t[3] > root_pos + 1:
            # We still have to loop
            pending.append((node, RIGHT, root_pos + 1, t[3]))

    return root_node


r = create_binary_tree(range(1,5))

