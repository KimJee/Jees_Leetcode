class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
            * We can always start a new [open paren] as long as we don't hit N
            * We [close paren] as long as we opened a [open paren] before and the count of it is correct
            * 
        """
        stack = []
        result = []
        
        def recursive_parenthesis(openN, closedN) -> str:
            
            # If we're out of characters
            if (openN == closedN == n):
                result.append("".join(stack))

            if (openN < n):
                stack.append("(")
                recursive_parenthesis(openN + 1, closedN)
                stack.pop()
            
            if (closedN < openN):
                stack.append(")")
                recursive_parenthesis(openN, closedN + 1)
                stack.pop()
        
        recursive_parenthesis(0, 0)
        return result
        

                

                
                