class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product = product * nums[j]
            result[i] = product
        return result"""
        
        n = len(nums)
        result = [1] * n

        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1

        for i in range(n-1,-1,-1): #Starting from last
            result[i] *= postfix
            postfix *= nums[i]
        return result