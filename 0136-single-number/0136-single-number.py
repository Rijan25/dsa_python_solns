class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result=0
        for num in nums:
            result^=num
        return result    
        # most optimal xor operations
        # result=0
        # for num in nums:
        #     result^=num
        # return result

        # # Hashmap solutions
        # count={}
        # for num in nums:
        #     if num in count:
        #         count[num]+=1
        #     else:
        #         count[num]=1
        # return min(count,key=lambda key: count[key])            
        