from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        
        fruit_types = defaultdict(int)
        
        left = 0        
        for right in range(len(fruits)):
            fruit_types[fruits[right]] += 1
            
            while len(fruit_types) > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    del fruit_types[fruits[left]]
                    
                left += 1
            
            max_len = max(max_len, right - left + 1)
                
        return max_len