class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r] # Keep adding total with the number of r

            # Now we will iterate until we get the total gretar or equal to target....
            # Ohterwise we will slide our window and decrease the left pointer number and increment it

            while total >= target:
                res = min(r-l+1,res)
                total -= nums[l]
                l+=1
        return 0 if res == float("inf") else res