class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mins=nums[0]
        diff=-1
        for l in range(1,len(nums)):
            diff=max(diff,nums[l]-mins)
            mins=min(mins,nums[l])
        return diff  if diff!=0 else -1   

             
           

        