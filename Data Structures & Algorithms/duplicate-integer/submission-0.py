class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

# Brute Force soln

# Sort the list first and then in range 1 to last item if the current item is
# same as last item then we will return True otherwise it will retun False.
#        nums.sort()
#        for i in range(1,len(nums)):
#            if nums[i]==nums[i-1]:
#                return True
#        return False

# Optimal using hash set length

        return len(set(nums)) < len(nums)