class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for index,num in enumerate(nums):
            if num !=0:
                nums[index],nums[l]=nums[l],nums[index]
                l+=1

        # Revision
        # l=0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[l],nums[i]=nums[i],nums[l]
        #         l+=1
        # return nums   





        # l=0
        # for r in range(len(nums)):
        #     if nums[r]:
        #         nums[l],nums[r]=nums[r],nums[l]
        #         l+=1
        # return nums        

        # l =0
        # for r in range(len(nums)):
        #     if nums[r]:
        #         nums[l],nums[r]=nums[r],nums[l]
        #         l+=1
           
        # return nums 
             
       

          
       
