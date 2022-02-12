class Solution:
    def process(self, n: int) -> int:
        sum_ = 0
        for n in str(n):
            sum_ += int(n) ** 2
        return sum_
    
    def isHappy(self, n: int) -> bool:
        
        slow = fast = n
        
        while True:
            slow = self.process(slow)
            fast = self.process(self.process(fast))

            if slow == 1 or fast == 1:
                return True
            
            if slow == fast:
                return False

        
        