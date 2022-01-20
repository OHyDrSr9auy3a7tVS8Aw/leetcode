class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        
        counts = [0, 0]
        
        left = 0
        for right in range(len(nums)):
            
            counts[nums[right]] += 1
            
            while right - left + 1 - counts[1] > k:
                counts[nums[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        