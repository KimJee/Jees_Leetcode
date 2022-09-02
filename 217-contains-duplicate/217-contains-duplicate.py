class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for item in nums:
            if my_dict.get(item) is None:
                my_dict[item] = 1
            else:
                return True
        return False