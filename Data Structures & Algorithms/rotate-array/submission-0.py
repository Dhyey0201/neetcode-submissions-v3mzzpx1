class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
         # Bruteforce : 
        
        n = len(nums)
        k = k % n # If n = 5 and k =3 then k become 2

        while k : # Until k = 0 this loop will run
            temp = nums[n-1] # Tempe = last element
            for i in range(n-1,0,-1): # for i in range last element to first
                nums[i] = nums[i-1]
            nums[0] = temp
            k -= 1
TC = o(n^2) and SC = O(n)
            """
            # Optimal solution

        n = len(nums)
        k = k % n

        def reverse(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l,r = l + 1, r -1

        reverse(0,n-1)
        reverse(0, k-1)
        reverse(k,n-1)