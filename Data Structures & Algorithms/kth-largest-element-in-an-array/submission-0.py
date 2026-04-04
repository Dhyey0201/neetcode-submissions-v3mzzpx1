class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return heapq.nlargest(k,nums)[-1]

        nums.sort()
        return nums[len(nums) - k]