class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,item in enumerate(nums):
            if target-item in hashmap.keys():
                return [index,hashmap[target-item]]
            hashmap[item]=index    
   