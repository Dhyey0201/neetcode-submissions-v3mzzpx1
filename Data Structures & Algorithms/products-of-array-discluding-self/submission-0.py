class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        for i in range(n):
            pro = 1
            for j in range(n):
                if i==j:
                    continue
                pro = pro * nums[j]
            res[i] = pro

        return res