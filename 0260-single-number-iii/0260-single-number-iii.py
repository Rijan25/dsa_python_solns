class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for num in nums:
            xor^=num
        diff=xor&-xor
        result1=0
        result2=0
        for num in nums:
            if num & diff:
                result1^=num  
            else:
                result2^=num
        return [result1,result2]              
        