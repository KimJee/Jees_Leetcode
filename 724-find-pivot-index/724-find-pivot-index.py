class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_prefix = self.prefix_sum(nums)
        right_prefix = self.reverse(self.prefix_sum(self.reverse(nums))) 
        for i in range(len(nums)):
            if (left_prefix[i] == right_prefix[i]):
                return i
        return -1
        
    def prefix_sum(self, nums: List[int]):
        acc = 0
        result = []
        for num in nums:
            acc += num
            result.append(acc)
        return result
    
    def reverse(self, nums: List[int]):
        begin = 0
        end = len(nums)-1
        while (begin < end):
            temp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = temp
            begin = begin + 1
            end = end - 1
        return nums
        
        
            
        