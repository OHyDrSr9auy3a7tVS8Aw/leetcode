from collections import Counter, defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        min_substr = (0, math.inf)
        
        target_hist = Counter(t)
        target = len(target_hist)
        window_hist = defaultdict(int)
        matched = 0
        
        left = 0
        for right in range(len(s)):
            r = s[right]
            window_hist[r] += 1
            if r in t and target_hist[r] == window_hist[r]:
                matched += 1
                   
            while left <= right and matched == target:
                min_substr = min(min_substr, (left, right), key=lambda t: t[1] - t[0])
                l = s[left]
                window_hist[l] -= 1
                if l in target_hist and window_hist[l] < target_hist[l]:
                    matched -= 1
                left += 1

                
        if min_substr[1] == math.inf:
            return ""
        
        return s[min_substr[0]:min_substr[1]+1]
            
        