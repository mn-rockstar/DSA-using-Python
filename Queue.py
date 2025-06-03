# Program to implement queue using python
class Queue:
    def __init__(self):
        self.items = []
    
    def is_Empty(self):
        return len(self.items) == 0

    def enque(self,data):
        self.items.append(data)
    
    def deque(self):
        if not self.is_Empty():
            self.items.pop(0)
        else:
            return "The Queue is Empty"
    
    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
            return "The Queue is empty"