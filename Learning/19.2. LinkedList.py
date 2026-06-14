class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#! Example - 1 : Create Nodes using only Node Class
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# Link Nodes
node1.next = node2
node2.next = node3

# Traverse and print
current = node1

while current:
    print(current.data)
    current = current.next

# ------------------------------------------------------------
#! Example - 2 : LinkedList


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"New Node : {new_node}")
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.display()
