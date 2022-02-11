class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda interval: interval[0])
        
        ans = [intervals[0]]
        
        for b in intervals[1:]:
            a = ans[-1]
            
            if a[1] >= b[0]:
                ans.pop()
                ans.append([min(a[0], b[0]), max(a[1], b[1])])
            else:
                ans.append(b)
                
                
        return ans
        