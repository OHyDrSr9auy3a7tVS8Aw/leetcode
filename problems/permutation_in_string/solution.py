from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        target_hist = defaultdict(int)
        window_hist = defaultdict(int)
        
        for i in range(len(s1)):
            target_hist[s1[i]] += 1
            window_hist[s2[i]] += 1
            
        if window_hist == target_hist:
            return True

        for next_ in range(len(s1), len(s2)):
            prev = next_ - len(s1)
            
            window_hist[s2[prev]] -= 1
            window_hist[s2[next_]] += 1
            
            if window_hist[s2[prev]] == 0:
                del window_hist[s2[prev]]
                
            if window_hist == target_hist:
                return True
            
        return False
            
            
        