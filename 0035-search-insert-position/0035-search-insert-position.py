class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Optimized Solutions
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

        # Brute Force Approach
        # for index,val in enumerate(nums):
        #     if target==val:
        #         return index
        #     elif target not in nums:
        #         if target<val:
        #             return index
        # return len(nums)
