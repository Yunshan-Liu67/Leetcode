class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31
        INT_MIN = -2**31 -1
        ans = 0
        xabs = abs(x)
        
        while xabs > 0:
            ans *= 10
            ans += xabs % 10
            xabs = int(xabs/10)      
        
        ans = ans if x > 0 else -ans
        
        return ans if INT_MIN <= ans <= INT_MAX else 0