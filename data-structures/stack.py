class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self):
        return self.elements.pop()
    
    def isempty(self):
        return not self.elements

    def peek(self):
        if not self.elements: raise IndexError("The stack is empty!")
        else: return self.elements[-1]

    def __str__(self):
        return " ".join(map(str, self.elements))