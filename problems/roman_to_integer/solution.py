class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subs = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        total = 0
        
        prev = ""
        for i in s:
            sus = prev + i
            if sus in subs:
                total += subs[sus] - vals[prev] 
            else:
                total += vals[i]
                
            prev = i
            
        return total