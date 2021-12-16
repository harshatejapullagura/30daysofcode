# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:  # target sum check to find a number
                return [hm[target - nums[i]], i]
            else:
                hm[nums[i]] = i


sl = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sl.twoSum(nums,target))
