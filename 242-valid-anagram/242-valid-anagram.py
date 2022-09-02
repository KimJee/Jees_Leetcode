class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given two string s and t
            # Return true if
                # t is an anagram of s
                # False otherwise
        freq_list = {}
        for letter in s:
            if freq_list.get(letter) is not None:
                freq_list[letter] += 1
            else:
                freq_list[letter] = 1
        
        # Add everything to the frequency table
        
        for letter in t:
            if freq_list.get(letter) == None:
                return False
            else:
                freq_list[letter] -= 1
        
        # Verify that all the letters is 0
        
        for key in freq_list.keys():
            if (freq_list[key] != 0):
                return False
        return True

        