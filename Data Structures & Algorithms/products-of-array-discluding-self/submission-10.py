class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pref = 1
        suff = 1
        res = [0] * n

        for i in range(n):
            res[i] += pref
            pref *= nums[i]

        for j in range(n-1,-1,-1):
            res[j] *= suff
            suff *= nums[j]
        return res