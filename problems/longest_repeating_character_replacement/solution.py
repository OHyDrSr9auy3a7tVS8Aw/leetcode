from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        
        chars = defaultdict(int)
        max_repeat = 1
        
        left = 0
        for right in range(len(s)):
            r = s[right]
            chars[r] += 1
            max_repeat = max(max_repeat, chars[r])
            
            while right - left + 1 - max_repeat > k:
                l = s[left]
                chars[l] -= 1
                left += 1              
            
            max_len = max(max_len, right - left + 1)
        
        return max_len