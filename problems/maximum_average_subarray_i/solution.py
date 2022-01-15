class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_diff = curr_diff = 0
        
        for i in range(len(nums)-k):
            curr_diff -= nums[i]
            curr_diff += nums[i+k]
            if curr_diff > max_diff:
                max_diff = curr_diff
            
        return (sum(nums[:k]) + max_diff) / k