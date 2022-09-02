class Solution:
    def search_recursive(self, nums, target, begin, end) -> int:
        mid = (end - begin) // 2 + begin
        print(mid)
        if (begin < end):  
            print(begin, end, target, nums[mid])
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                return self.search_recursive(nums, target, begin, mid)
            elif (target > nums[mid]):
                return self.search_recursive(nums, target, mid+1, end)
            else:
                return "This never should happen."
        else:
            return -1
        
    def search(self, nums: List[int], target: int) -> int:
        return self.search_recursive(nums, target, 0, len(nums))
    
    
    
        
        
        
        
        