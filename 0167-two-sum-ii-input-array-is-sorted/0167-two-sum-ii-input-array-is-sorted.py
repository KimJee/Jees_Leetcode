class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use the two-pointer method
        low, high = 0, len(numbers) - 1
        while (low < high):
            sum = numbers[low] + numbers[high]
            # print(low, numbers[low], high, numbers[high], sum)
            if (sum == target):
                return [low + 1, high + 1]
            elif (sum < target):
                low += 1
            else: # (sum > target)
                high -= 1


        
