class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}
        for index, num in enumerate(nums):
            if (complement.get(num) is None):
                comp = target - num
                complement[comp] = index
            else:
                return index, complement[num]
        print(complement)
            
            
            
        