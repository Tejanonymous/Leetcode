class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=[0]*(m+n)
        i=0
        j=0
        k=0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                l[k]=nums1[i]
                i+=1
            else:
                l[k]=nums2[j]
                j+=1
            k+=1
        while i<m:
            l[k]=nums1[i]
            i+=1
            k+=1
        while j<n:
            l[k]=nums2[j]
            j+=1
            k+=1   
        nums1[:]=l   
                
                