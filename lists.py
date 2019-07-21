# dummy change 6
class Node(object):
    def __init__(self, val, nxt=None):
        self.value = val
        self.nxt = nxt


def remove_node(node):
    if node is None:
        return
    temp = node.nxt
    if temp is not None:
        node.value = temp.value
        node.nxt = temp.nxt
        del temp
    else:  # Last element
        node = None


def print_list(node):
    while node is not None:
        print node.value
        node = node.nxt


def mergeSort(mylist):
    if len(mylist) <= 1:
        return mylist
    pending = []
    for i in mylist:
        pending.append([i])
    while len(pending) > 1:
        # Merge two first lists
        l1 = pending.pop()
        l2 = pending.pop()
        lr = [None] * (len(l1) + len(l2))
        i = j = k = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                lr[k] = l1[i]
                i += 1
            else:
                lr[k] = l2[j]
                j += 1
            k += 1
        # End of list
        if i == len(l1):
            while k < (len(l1) + len(l2)):
                lr[k] = l2[j]
                k += 1
                j += 1
        else:
            while k < (len(l1) + len(l2)):
                lr[k] = l1[i]
                k += 1
                i += 1
        pending.append(lr)
    return pending[0]

# n4 = Node(4)
# n3 = Node(3, n4)
# n2 = Node(2, n3)
# n1 = Node(1, n2)
#
# remove_node(n4)
# print_list(n1)

l = [54,26,93,17,77,31,44,55,20]
l2 = mergeSort(l)
l2[0]
