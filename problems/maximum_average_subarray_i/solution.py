class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # [1,2,3,4] k=2
        # 1,2; 2,3; 3,4;
        
        sum_ = sum(nums[:k])
        max_sum = sum_
        
        for nxt in range(k, len(nums)):
            prv = nxt - k
            sum_ -= nums[prv]
            sum_ += nums[nxt]
            
            max_sum = max(max_sum, sum_)
            
        return max_sum / k