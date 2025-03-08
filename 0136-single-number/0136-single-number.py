class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        return min(count,key=lambda key: count[key])            
        