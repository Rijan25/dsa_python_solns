class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index,val in enumerate(nums):
            if target==val:
                return index
            elif target not in nums:
                if target<val:
                    return index
        return len(nums)        

         

        