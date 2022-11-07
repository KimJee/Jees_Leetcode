class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.memoization(nums)
    
    def brute_force(self, nums:List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            for k in range(i):
                product = product*nums[k]
            for j in range(i+1, len(nums)):
                product = product*nums[j]
            result.append(product)
        return result
    
    def memoization(self, nums:List[int]) -> List[int]:
        
        # Prefix iteration
        result = [1]*(len(nums)+1)
        for i in range(1, len(nums) + 1, 1):
            result[i] = nums[i-1]*result[i-1]
        print(result)
        
        product = 1
        for j in range(len(nums)-1, -1, -1):
            product = product*nums[j]
            result[j-1] = product*result[j-1]
        # Postfix iteration
        # product = 1
        # for j in range(len(result)-2, -1, -1):
        #     product = product*nums[j]
        #     result[j] = result[j]*product
        return result[:-1]
            
    
        
    
            
        
        # result
        
        
                
        