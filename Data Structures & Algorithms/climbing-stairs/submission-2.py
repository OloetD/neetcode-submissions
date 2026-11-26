class Solution:
    def climbStairs(self, n: int) -> int:
        pprev, prev = 0,1
        r = prev+pprev
        for _ in range(2, n+1):
            prev, pprev = r, prev
            r = prev+pprev
        return r