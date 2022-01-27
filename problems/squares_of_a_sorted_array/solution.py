import math

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [None] * n

        left = 0
        right = n - 1
        
        for i in range(n - 1, -1, -1):
            left_val = nums[left] ** 2
            right_val = nums[right] ** 2
            
            if left_val > right_val:
                ans[i] = left_val
                left += 1
            else:
                ans[i] = right_val
                right -= 1
        
        return ans