from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        anagrams = list()
        
        target_hist = defaultdict(int)
        window_hist = defaultdict(int)

        for i in range(len(p)):
            target_hist[p[i]] += 1
            window_hist[s[i]] += 1
            
        
        if window_hist == target_hist:
            anagrams.append(0)
        
        for nxt in range(len(p), len(s)):
            prev = nxt - len(p)
            
            window_hist[s[prev]] -= 1
            window_hist[s[nxt]] += 1
            
            if window_hist[s[prev]] == 0:
                del window_hist[s[prev]]
                
            if window_hist == target_hist:
                anagrams.append(prev + 1)
                
        return anagrams
        
        