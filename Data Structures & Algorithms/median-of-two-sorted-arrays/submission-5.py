class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        for i in range(len(nums1)):
            temp.append(nums1[i])
        for j in range(len(nums2)):
            temp.append(nums2[j])

        temp.sort()

        n = len(temp)
        print(n)

        if n % 2==0:
            return (temp[n // 2 - 1] + temp[n // 2]) / 2
        else:
            return temp[n//2]