class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Hashmap Method
        from collections import Counter
        counts=Counter(nums)
        majority=len(nums)//2
        for num in nums:
            if counts[num]>majority:
                return num

        # # Boyer Moore Voting Algorithm

        # count,result=0,0
        # for num in nums:
        #     if count==0:
        #         result=num
        #     else:
        #         count+=(1 if result==num else -1) 
        # return result           


        # # count={}
        # # majority=len(nums)//2
        # # for num in nums:
        # #     if num in count:
        # #         count[num]+=1
        # #     else :
        # #         count[num]=1
        # #     if count[num]>majority:
        # #         return num    
      
                        

        # # Boyer Moore Voting Algorithms

        # # count,result=0,0
        # # for num in nums:
        # #     if count==0:
        # #         result=num
        # #     else:
        # #         count+=(1 if result==num else -1)  
        # # return result        


        
        # # Hashmap
        # # count={}
        # # majority=len(nums)//2
        # # for num in nums:
        # #     if num in count:
        # #         count[num]+=1
        # #     else:
        # #         count[num]=1
        # #     if(count[num]>majority):
        # #         return num    
                


        

        