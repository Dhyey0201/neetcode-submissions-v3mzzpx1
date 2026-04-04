class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            i = L
            j = 0
            k = 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j+=1
                else:
                    nums[i] = right[k]
                    k+=1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i +=1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i +=1
        def mergesort(arr,l,r):
            if l == r:
                return arr
            m = (l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        return mergesort(nums,0,len(nums) - 1)

        
            