class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        
        curr_sum = None
        
        while curr_sum != target:
            left = numbers[l]
            right = numbers[r]
            
            curr_sum = left + right
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            
        return [l+1, r+1]