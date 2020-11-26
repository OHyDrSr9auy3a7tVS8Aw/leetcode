class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            complement = target - n
            try:
                j = h[complement]
                if i != j:
                    return [i, j]
            except KeyError:
                h[n] = i