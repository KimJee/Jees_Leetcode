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
        result = []
        
        prefix_product = []
        product = 1
        for i in range(len(nums)):
            product = product*nums[i]
            prefix_product.append(product)
        
        postfix_product = []
        product = 1
        for j in range(len(nums)-1, -1, -1):
            product = product*nums[j]
            postfix_product.insert(0, product)
        
        print(prefix_product)
        print(postfix_product)
        
        result = []
        result.append(postfix_product[1])
        for k in range(1, len(nums) -1, 1): 
            result.append(prefix_product[k-1]*postfix_product[k+1])
        result.append(prefix_product[len(nums)-1-1])    
        print(result)
            
        
        
        return result
        
        
                
        