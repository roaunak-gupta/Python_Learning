class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def nQueue(self, value):
        if len(self.queue) == 0:
            self.front = self.front + 1
            self.rear = self.rear + 1
            self.queue.insert(self.rear, value)
        else:
            self.rear = self.rear + 1
            self.queue.insert(self.rear, value)
        print(self.queue, self.front, self.rear)

    def dQueue(self):
        if len(self.queue) == 0:
            raise Exception("Your Queue is Empty...")
        else:
            self.rear = self.rear - 1
            print(f"Dequeue : {self.queue.pop(0)}")

    def display_all(self):
        for element in range(0, len(self.queue)):
            print(self.queue[element], end=" | ")


queue = Queue()
queue.nQueue(10)
queue.nQueue(20)
queue.nQueue(30)
queue.nQueue(40)
queue.nQueue(50)
queue.dQueue()
queue.nQueue(60)
queue.nQueue(70)
queue.nQueue(80)
queue.nQueue(90)
queue.nQueue(100)
queue.dQueue()
queue.nQueue(110)
queue.nQueue(120)
queue.dQueue()
queue.display_all()
