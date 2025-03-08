class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=0
        ret_digits=[]
        for index,num in enumerate(digits):
            result=result*10+num
        final_list=[int(x) for x in str(result+1)]
        return final_list
        