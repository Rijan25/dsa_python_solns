class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        count={}
        nums.sort()
        for num in nums:
            if num in count and num%2==0:
                count[num]+=1
            elif num not in count and num%2==0:
                count[num]=1
        if(len(count)==0):
            return -1
        return (max(count,key=lambda key:count[key]))            


        # count={}
        # nums.sort()
        # for num in nums:
        #     if num in count and num%2==0:
        #         count[num]+=1
        #     elif num not in count and num%2==0:
        #         count[num]=1
        # if len(count)==0:
        #     return -1
        # return max(count,key=lambda key:count[key])            

        