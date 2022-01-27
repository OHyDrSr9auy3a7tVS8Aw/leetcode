class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        l = 0
        for r in range(1, len(nums)):
            left, right = nums[l], nums[r]
            
            if left != right:
                l += 1
                nums[l] = right
                k += 1
            
        return k