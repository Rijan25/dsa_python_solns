class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,num in enumerate(nums):
            for i in range(index+1,len(nums)):
                if (target-num)==nums[i]:
                    return [index,i]
        
            
        