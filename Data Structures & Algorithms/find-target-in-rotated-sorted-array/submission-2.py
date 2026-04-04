class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force gives Time comlexity = O(n)
        #for i in range(len(nums)):
        #    if nums[i] == target:
        #        return i
        #return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
# sorting and searching the left side of the array
            if nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
# sorting and searching the right side of the array
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1