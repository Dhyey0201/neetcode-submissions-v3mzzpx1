class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in nums:
            count = sum(1 for j in nums if j == i)
            if count > n//2:
                return i