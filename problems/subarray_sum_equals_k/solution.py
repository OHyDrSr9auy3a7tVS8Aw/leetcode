from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = defaultdict(int)
        sums[0] = 1
        count = sum_ = 0
        
        for num in nums:
            sum_ += num
            count += sums[sum_-k]
            sums[sum_] += 1
                
        return count
        