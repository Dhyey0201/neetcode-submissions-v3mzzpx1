class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        op = []

        for i in range(len(nums) - k + 1):
            maximum = nums[i]
            for j in range(i, i + k):
                maximum = max(maximum, nums[j])
            op.append(maximum)
        return op