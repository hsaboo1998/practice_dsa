# stack using linked list
class Node(value):
    def __init__(self):
        self.value = value
        self.next = None

class Stack()
    def __init__(self):
        self.head = None
        self.size=0
    def push(value):
        nn = Node(value)
        nn.next = self.head
        self.head = nn
        self.size+=1
    def pop():
        if self.isEmpty:
            print("Empty stack")
        else:
            pop_val = self.head.value
            self.head = self.head.next
            self.size-=1
            return pop_val