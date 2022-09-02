class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) == 0 or len(s) == 1):
            return True
        
        '''Strip away non-characters and make homogenous'''
        s = s.lower()
        new_string = []
        for char in s:
            if (char.isalpha() or char.isnumeric()):
                new_string.append(char)
        
        '''Comparison between the string'''
        begin = 0
        end = len(new_string) - 1
        
        while (begin < end):
            first_letter = new_string[begin]
            last_letter = new_string[end]
            print(first_letter, last_letter)
            if (first_letter != last_letter):
                return False
            begin += 1
            end -= 1
        return True
            
            