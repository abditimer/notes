# Create Linked List 
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # if we want to add a link
        if nodes is not None:
            # remove first item from list and set as head node
            node = Node(data=nodes.pop(0))
            self.head = node
            # create nodes for remainder of items
            for elem in nodes:
                # set the next node
                node.next = Node(data=elem)
                # set next node as our current node
                node = node.next
    # This must be implemented to make this object iterable 
    # e.g. use: for i in linked_list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # inserting at beginning
    def add_first(self, node):
        node.next = self.head
        self.head = node

    
    # The below helps visualise what is happening
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next 
        nodes.append('None')
        return ' -> '.join(nodes)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data





######################################

# llist = LinkedList()
# print(llist)

# node_1 = Node('a')
# llist.head = node_1
# print(llist)

# node_2, node_3 = Node('b'), Node('c')
# node_1.next = node_2
# node_2.next = node_3 
# print(llist)


l_list = LinkedList(['1','2','3','4','5'])
print(l_list)

for node in l_list:
    print(node)

l_list.add_first(Node('first!'))
print(l_list)

l_list.add_first(Node('No me!!!!'))
print(l_list)