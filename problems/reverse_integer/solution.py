class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        s = str(abs(x))[::-1]
        x = int(s)
        if (x > 2**31 - 1) or (x < -2**31):
            return 0
        if neg:
            return -x
        else:
            return x
        