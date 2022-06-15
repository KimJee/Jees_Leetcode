class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            One way to approach this problem is to sort the array
            But the easiest way I think is to use a hash table and if the value is found return it immediatly
        """
        
        history = {}
        for index in range(len(nums)):
            number = nums[index]
            if (number in history):
                return True
            else:
                history[number] = 1
            #print(history)
        return False
    