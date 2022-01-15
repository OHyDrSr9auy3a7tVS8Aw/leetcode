class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_sub_idx = 0
        max_ = nums[0]
   
        for i in range(len(nums)-k+1):
            curr_first = nums[i]
            
            if curr_first > max_:
                max_ = curr_first
                max_sub_idx = i
            
        return nums[max_sub_idx:max_sub_idx+k]