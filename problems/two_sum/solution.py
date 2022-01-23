class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        
        for i, num in enumerate(nums):
            complement = target - num
            
            try:
                comp_idx = seen[complement]
                if comp_idx != i:
                    return [comp_idx, i]
            except KeyError:
                seen[num] = i