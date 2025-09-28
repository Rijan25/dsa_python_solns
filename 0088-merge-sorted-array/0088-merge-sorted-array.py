class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Two Pointers Approach
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        
        # for the remaining elements of the small nums2
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1







        
        # Simple Sorted
        # for j in range(n):
        #     nums1[m+j]=nums2[j]
        # nums1.sort()    
         

        