from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        
        uniq_chars = defaultdict(int)
        
        left = 0        
        for right in range(len(s)):
            uniq_chars[s[right]] += 1
            
            while len(uniq_chars) > 2:
                uniq_chars[s[left]] -= 1
                if uniq_chars[s[left]] == 0:
                    del uniq_chars[s[left]]
                    
                left += 1
            
            max_len = max(max_len, right - left + 1)
                
        return max_len