class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hist = dict()
        for num in nums: 
            if hist.get(num) is None:
                hist[num] = 1
            else:
                return True
        return False
        
        