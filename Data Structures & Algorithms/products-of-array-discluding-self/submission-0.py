class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        pre = 1
        suff = 1
        n = len(nums)
        for i in range(n):
            out[i] = out[i] * pre
            out[n-1-i] *= suff
            suff *= nums[n-1-i]
            pre *= nums[i]

        return out