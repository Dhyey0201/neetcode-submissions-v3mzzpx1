class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        current = [0]
        streak = 0
        i = 0

        while i<len(nums):
            if current != nums[i]:
                current = nums[i]
                streak = 0
            while i<len(nums) and nums[i]==current:
                i = i+1
            streak = streak + 1
            current = current + 1
            res = max(res , streak)
        return res