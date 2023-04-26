
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            (1) Add numbers to the stack until I get an operation.
                (a) "+", "-", "/", "*"
            (2) When I get the operation then I want to pop off two of the most recent numbers
            (3) Apply the operation
            (4) Store result back into that stack
            (5) Repeat the process until I reach the end of the tokens list.
        """
        result = 0
        stack_list = []

        # Easy Way
        # stack_pop() ==> stack_list.pop(0)
        # stack_push() ==> stack_list.insert(0, value)
        # stack_top() ==> stack_list[0]

        for token in tokens:
            # (1) Add numbers to the stack until I get an operation.
            if (token not in ["+", "-", "/", "*"]):
                stack_list.insert(0, token)
            else:
                first_argument = int(stack_list[0])
                stack_list.pop(0)
                second_argument = int(stack_list[0])
                stack_list.pop(0)
                
                subexpression = 0
                if (token == "+"):
                    subexpression = first_argument + second_argument
                elif (token == "-"):
                    subexpression = second_argument - first_argument
                elif (token == "*"):
                    subexpression = first_argument * second_argument
                else: #(token == "/")
                    subexpression = second_argument / first_argument
                # print(second_argument, token, first_argument, subexpression)
                stack_list.insert(0, subexpression)
                    
        return int(stack_list[0])

        

        # Create a "custom stack class" 
