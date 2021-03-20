class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        seen = []
        
        for _s in s:
            if _s in seen:
                seen = seen[seen.index(_s) + 1:]
                
            seen.append(_s)
            print(seen)
                
            l = len(seen)
            if l > longest:
                longest = l
                
                
        
        return longest