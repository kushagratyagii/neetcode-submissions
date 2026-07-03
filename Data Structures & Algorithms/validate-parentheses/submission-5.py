class Stack:

    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
         return self.stack.pop()

    

    def empty(self):
        return len(self.stack)==0
    def top(self):
        
        return self.stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        obj = Stack()
        if s =="":
            return True
        l = {')':'(',']':'[','}':'{'}
        
        for i in s:
            if i in l:
                if not obj.empty() and obj.top() == l[i]:
                    obj.pop()
                else:
                    return False
            else:
                obj.push(i)

        if obj.empty():
            return True
        
        return False
                
