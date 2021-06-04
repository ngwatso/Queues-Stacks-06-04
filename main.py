class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        
        temp = []
        
        while left.isEmpty() == False:
            right.push(left.pop())
            
        temp.append(right.pop())
        
        while right.isEmpty() == False:
            left.push(right.pop())
            
        return temp.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans

# ===============

class Stack:
    
    def __init__(self):
        self.items = []
            
    def push(self, item):
        self.items.append(item)
            
    def pop(self):
        return self.items.pop()

def validBracketSequence(sequence):
    
    openBracket = Stack()
    values = {'(':1, ')':1, '[':2, ']':2, '{':3, '}':3}
    tempO = []
    tempC = []
    
    if len(sequence) % 2 != 0:
        return False
    
    for i in sequence:
        
        if i == '(' or i == '[' or i == '{':
            openBracket.push(i)
        elif i == ')' or i == ']' or i == '}':
            
            if sequence.index(i) == 0:
                return False
                
            tempC.append(i)
            tempO.append(openBracket.pop())
            
            if (values[tempO[0]] != values[tempC[0]]):
                return False
            else:
                tempO = []
                tempC = []
                
    return True