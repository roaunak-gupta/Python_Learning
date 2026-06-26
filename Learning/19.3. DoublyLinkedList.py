class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.teal = None
        print("New Doubly Linked List is Created as Succesfully...")

    def display_forword(self):
        current = self.head

        print("Head", end=" -> ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Teal")

    def display_backword(self):
        current = self.teal
        print("Teal", end=" <- ")
        while current:
            print(current.data, end=" <- ")
            current = current.previous
        print("Head")

    def insert_on_teal(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"First Node Created.")
            return
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current
        self.teal = new_node

    def insert_on_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"First Node Created with the data : {new_node.data}")
            return

        temp = self.head

        new_node.next = self.head
        temp.previous = new_node
        self.head = new_node

    def insert_on_mid(self, data, location):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"First Node Created with the data : {new_node.data}")
            return

        current = self.head

        while current:
            if current.data == int(location):
                new_node.next = current.next
                new_node.previous = current
                if current.next:
                    print(current.next.previous.data)
                    current.next.previous = new_node
                else:
                    self.teal = new_node
                current.next = new_node
                return
            current = current.next

    def delete_node(self, location):
        current = self.head
        while current:
            if current.data == int(location):
                if current == self.head:
                    self.head = current.next
                    if current.next:
                        current.next.previous = None
                        print(current.data,": Head Deleted.")
                else:
                    if current == self.teal:
                        current.previous.next = None
                        self.teal = current.previous
                        print(current.data,": Teal Deleted.")
                    else:
                        current.previous.next = current.next
                        current.next.previous = current.previous
                        print(current.data,": MID Deleted.")
            current = current.next


dll = DoublyLinkedList()
dll.insert_on_teal(2)
dll.insert_on_teal(4)
dll.insert_on_teal(6)
dll.insert_on_teal(8)
dll.insert_on_teal(10)
dll.insert_on_teal(12)
dll.insert_on_teal(14)
dll.insert_on_head(1)
dll.insert_on_teal(16)
dll.insert_on_teal(18)
dll.insert_on_mid(15, 14)
dll.insert_on_teal(20)
dll.insert_on_teal(22)
dll.display_forword()
dll.display_backword()
dll.delete_node(12)
dll.display_forword()
dll.display_backword()
