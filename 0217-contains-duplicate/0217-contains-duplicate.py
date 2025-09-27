class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for index,num in enumerate(nums):
            if num in hash:
                return True
            hash[num]=index
        return False        
        