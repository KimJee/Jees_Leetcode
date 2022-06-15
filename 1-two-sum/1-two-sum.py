dict = {}


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        history = {}
        for (i, item) in enumerate(nums):
            if item in history:
                return [i, history[item]]
            
            complement = target - item
            history[complement] = i
            
            # print(f"Current Item: {item} | Complement: {complement} | History: {history}")
            
            
    
            
            
        