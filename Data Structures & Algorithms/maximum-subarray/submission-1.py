class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = 0
        maxsum = nums[0]

        for num in nums:
            if res < 0:
                res = 0
            res += num
            maxsum = max(maxsum, res)
        return maxsum

        