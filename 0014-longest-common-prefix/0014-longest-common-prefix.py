class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "" 
        
        # Find out the shortest string in strs
        
        min_length = len(strs[0])
        for _string in strs:
            min_length = min(len(_string), min_length)
        
        longest_prefix = ""
        for i in range(min_length):
            match_char = strs[0][i]
            for word in strs:
                if (word[i] != match_char):
                    return longest_prefix
            longest_prefix += match_char
        return longest_prefix
                    



        
            


            
