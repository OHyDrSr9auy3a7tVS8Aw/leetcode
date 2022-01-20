from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        
        left = 0
        
        chars = defaultdict(int)
        
        for right in range(len(s)):
            chars[s[right]] += 1
  
            while len(chars) > k:
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
        
        return max_len
            
            
        