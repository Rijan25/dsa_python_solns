class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Optimal Solutions using reversal
        n=len(nums)
        k%=n
        def reverse_array(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

            reverse_array(0,n-1)
            reverse_array(0,k-1)
            reverse_array(k,n-1)    



        # Extra Space 
        n=len(nums)
        rotated=[0]*n
        for index,num in enumerate(nums):
            rotated[(index+k)%n]=nums[index]
        nums[:]=rotated
        return nums    


        