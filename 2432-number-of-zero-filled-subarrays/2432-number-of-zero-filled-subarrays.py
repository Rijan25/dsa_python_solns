class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result=0
        count=0
        for num in nums:
            if num==0:
                count+=1
                
            else:
                result+=count*(count+1)//2 
                count=0
        # For Accounting the contibution of the last zero        
        result+=count*(count+1)//2         
              
        return result         
        