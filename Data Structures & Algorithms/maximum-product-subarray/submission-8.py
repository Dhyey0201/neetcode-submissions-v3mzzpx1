class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1,1
        result = max(nums)

        for n in nums:
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin  = min(temp, n * curMin, n)
            result = max(result, curMax)
        return result