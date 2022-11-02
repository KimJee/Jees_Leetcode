class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hist = {}
        for letter in s:
            if hist.get(letter) is None:
                hist[letter] = 1
            else:
                hist[letter] += 1
        # print(hist)
        
        for letter in t:
            if hist.get(letter) is None:
                return False
            else:
                hist[letter] -=  1
        
        for count in hist.values():
            if (count != 0):
                return False
        return True
        