class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.insert(0, value)
        print(f"{value} : Inserted on Stack.")

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty...")
        else:
            return self.stack.pop(0)

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty...")
        else:
            return self.stack[0]

    def length(self):
        print(f"Length of Stack : {len(self.stack)}")

    def display_all(self):
        for element in range(0,len(self.stack)):
            print(self.stack[element])


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)
stack.push(90)
stack.push(100)
stack.display_all()
print(f"Peek Element : {stack.peek()}")
stack.pop()
stack.display_all()
