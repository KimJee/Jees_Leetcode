class Solution:
    def isValid(self, s: str) -> bool:
        stack = MyStack()

        for letter in s:
            # First check if the stack has anything
            # print(letter, stack.top(), "Stack:", stack.stack)
            if (letter in ["[", "(", "{"]):
                stack.push(letter)
            else:
                if (stack.top() == "[" and letter == "]"):
                    stack.pop()
                elif (stack.top() == "(" and letter == ")"):
                    stack.pop()
                elif (stack.top() == "{" and letter == "}"):
                    stack.pop()
                else:
                    return False
        if (stack.getSize() != 0):
            return False
        return True


                
    

                
        
        
class MyStack:
        def __init__(self):
            self.stack = []
            self.size = 0
        
        def push(self, obj):
            self.stack.insert(0, obj)
            self.size += 1
        
        def pop(self):
            if (self.size == 0):
                 print("Cannot Pop an empty stack")
            else:
                self.stack.pop(0)
                self.size -= 1
        
        def top(self):
            if (self.size == 0):
                return ""
            else:
                return self.stack[0]
        
        def getSize(self):
            return self.size

