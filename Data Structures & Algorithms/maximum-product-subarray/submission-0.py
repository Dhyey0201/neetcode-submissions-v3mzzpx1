class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n #bug - We declare temp so that we can use it in curMin calculation

            curMax = max(curMax * n, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res