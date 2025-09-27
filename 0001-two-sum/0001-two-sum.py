class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach
        # for index,num in enumerate(nums):
        #     for i in range(index+1,len(nums)):
        #         if (target-num)==nums[i]:
        #             return [index,i]

        
        # HashTable Approach
        hashtable={}
        n=len(nums)

        for index,num in enumerate(nums):
            complement=target-num
            if complement in hashtable:
                return [index,hashtable[complement]]
            hashtable[num]=index    

        
            
        