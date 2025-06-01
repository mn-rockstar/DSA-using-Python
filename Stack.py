# code for implementing for stack in python
class Stack:

    # initializing the empty list
    def __init__(self):
        self.items = []
    
    # method to check if the list is empty or not
    def is_Empty(self):
        return len(self.items) == 0
    
    # method to add element at last
    def add(self,data):
        self.items.append(data)

    # method to remove the element from last
    def remove(self):
        if not self.is_Empty():
            self.items.pop()
        else:
            return "The Stack is empty"
        
    # method to get the top element from the stack 
    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
            return "The stack is empty"
        

# creating the object
s1 = Stack()
s1.add(1)
print(s1.items)
s1.add(2)
print(s1.items)
s1.add(3)
print(s1.items)
s1.add(4)
print(s1.items)
s1.remove()
print(s1.items)
s1.remove()
print(s1.items)

print(s1.peek())