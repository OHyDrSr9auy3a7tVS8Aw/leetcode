class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        chars_rightmost_pos = {}
        
        left = 0
        for right in range(len(s)):
            r = s[right]
            
            if r in chars_rightmost_pos:
                # skip straight ahead past dupe
                left = max(chars_rightmost_pos[r] + 1, left)
    
            max_len = max(max_len, right - left + 1)
            chars_rightmost_pos[r] = right
            
        return max_len