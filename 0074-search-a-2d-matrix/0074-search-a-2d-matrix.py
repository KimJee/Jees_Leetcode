class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        bot, top = 0, rows - 1
        while (bot <= top):
            middle = (top + bot) // 2
            if (target < matrix[middle][0]):
                top = middle - 1
            elif (target > matrix[middle][-1]):
                bot = middle + 1
            else:
                break
        if (bot > top):
            return False
        
        return self.binary_search(matrix[middle], target)




    def binary_search(self, my_list, target):
        l, r = 0, len(my_list) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (target < my_list[mid]):
                r = mid - 1
            elif (target > my_list[mid]):
                l = mid + 1
            else:
                return True
        return False
