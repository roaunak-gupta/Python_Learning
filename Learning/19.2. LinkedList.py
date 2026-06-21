class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        print("New LinkedList is Created as Succesfully...")

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_on_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"First Node Element : {new_node.data}")
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_on_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"First Node Element : {new_node.data}")
            return

        new_node.next = self.head
        self.head = new_node

    def insert_on_mid(self, data, location):

        new_node = Node(data)
        current = self.head
        while current:
            if current.data == location:
                temp = current.next
                current.next = new_node
                new_node.next = temp
                print(f"Node {new_node.data} Inserted after : {current.data}")
                break
            current = current.next

    def delete_node(self, value):

        head = self.head
        current = self.head
        previous_node = self.head
        while current:
            if current.data == int(value):
                if current == head:
                    self.head = current.next
                    print(f"Head Element {head.data} Deleted.")
                    del current
                else:
                    if current.next == None:
                        while previous_node:
                            if previous_node.next == current:
                                previous_node.next = None
                                del current
                                print(f"Last Element Deleted.")
                            previous_node = previous_node.next
                    else:
                        while previous_node:
                            if previous_node.next == current:
                                previous_node.next = current.next
                                print(f"Mid Element {current.data} Deleted.")
                                del current
                                break
                            previous_node = previous_node.next
                break
            current = current.next


ll = LinkedList()
ll.insert_on_end(10)
ll.insert_on_end(20)
ll.insert_on_end(30)
ll.display()
ll.insert_on_mid(15, 10)
ll.display()
ll.insert_on_end(40)
ll.insert_on_end(50)
ll.display()
ll.insert_on_start(5)
ll.delete_node(5)
ll.display()
