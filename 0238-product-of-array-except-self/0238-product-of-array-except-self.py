class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Optimal Solutions ( TC 0n and SC 01)
        n=len(nums)
        suffix=1
        product_array=[1]*n
        for i in range(1,n):
            product_array[i]=nums[i-1]*product_array[i-1]
        for i in range(n-2,-1,-1):
            suffix*=nums[i+1]
            product_array[i]*=suffix  
        return product_array    
              



        # Brute Force Approach
        # product_array=[]
        # n=len(nums)
        # for i in range(n):
        #     product=1
        #     for j in range(n):
        #         if i!=j:
        #             product=product*nums[j]
        #     product_array.append(product)     
        # return product_array       

        
              

         


        