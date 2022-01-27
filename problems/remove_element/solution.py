class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        last = len(nums) - 1
        
        while l <= last:
            if nums[l] == val:
                if l == last:
                    nums.pop()
                else:
                    nums[l] = nums.pop()
                last -= 1
            else:
                l += 1

        return last + 1