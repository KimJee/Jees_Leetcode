class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            One way may be the multiply all the numbers together
            And divide out the number in the particular index
        """
        return self.fourth_attempt(nums)
        
    """
        OOPS Apperently I can't use the division operation!
        Plus this won't work if there is a single 0, as the division wouldn't make the test case fail
    """
    def first_attempt(self, nums: List[int]) -> List[int]:
        
        output_array = []
        total_multiplicative = 1
        for num in nums:
            total_multiplicative = num*total_multiplicative
        
        for i in range(len(nums)):
            output_array.append(int(total_multiplicative/nums[i]))
        
        print(output_array)
        return output_array
    
    def second_attempt(self, nums: List[int]):
        
        # Probably use array slicing...
        
        result = []
        for i in range(len(nums)):
            front = nums[:i]  
            # print(front)
            back = nums[i+1:]
            # print(back)
            
            
            front_total = self.multiply_subarray(front)
            back_total = self.multiply_subarray(back)
            
            total_multi = front_total * back_total
            
            result.append(total_multi)
        
        return result
    
    """
        This is inefficient, I can use dynamic programming to store a prefix/subfix total and reuse that total to multiply the subarray
    """
    def multiply_subarray(self, nums:List[int]) -> int:
        if not nums:
            return 1
        else:
            total = 1
            for num in nums:
                # print(f"{total}, {num}, {nums}")
                total = total*num
            return total
        
    def third_attempt(self, nums: List[int]) -> List[int]:
        """
            Now using dynamic programming to store prefix and suffixes
        """
        
        lookup_table = self.setup_memoization_table(nums)
        result_list = []
        for i in range(len(nums)):
            result_list.append(self.find(i, lookup_table, len(nums)))
        return result_list
    
    def fourth_attempt(self, nums: List[int]) -> List[int]:
        """
            Just multiply the prefix and the suffixes
        """
        res = [1 for _ in range(len(nums))]
        #  get every product from the left for each index
        leftRunningProduct = 1
        for i in range(len(nums)):
            res[i]  = leftRunningProduct
            leftRunningProduct *= nums[i]
         # mutiply every product from the right for each index
        rightRunningProduct = 1
        for i in reversed(range(len(nums))):
            res[i] *= rightRunningProduct
            rightRunningProduct *= nums[i]
        return res
        
        
    
    def setup_memoization_table(self, nums):
        
        rows, cols = len(nums)+1, len(nums)+1
        arr = []
        for i in range(len(nums)+1):
            row = []
            for j in range(len(nums)+1):
                row.append(1)
            arr.append(row)
        
        
        for k in range(len(nums)):
            arr[1][k+1] = nums[k]
            #print(arr)
        
        for i in range(2, rows, 1):
            for j in range(2, cols, 1):
                arr[i][j] = arr[i-1][j-1] * arr[1][j]
        print(arr)
        
        return arr
    
    
    def find(self, i, memoization_table, n) -> int:
        #  [0][1][2][3][4]
        #   0   0  0   0   0   0 
        #   0 [ 2, 3,  4,  5,  6 ]
        #   0 [    6, 12, 20, 30 ]
        #   0 [       24, 60, 120]
        #   0 [          120, 360]
        #   0 [               720]
        #   0 [ 360, 240, 180, 144, 120 ]
        # n = 5 i = 1 a[i] = 3
        prefix_total = memoization_table[i][i]
        postfix_total = memoization_table[n-i-1][n]
        print(f'Prefix_total: {prefix_total} | Postfix_total: {postfix_total}')
        total = prefix_total*postfix_total
        return total
    
        
        
        