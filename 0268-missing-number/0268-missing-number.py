class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Optimal Solutions using Brute force approach
        n=len(nums)
        sum=0
        total_sum=(n*(n+1))//2
        for num in nums:
            sum+=num
        return total_sum-sum
        # Brute Force Approach
        for index in range(len(nums)+1):
            if index not in nums:
                return index
                    




        

        