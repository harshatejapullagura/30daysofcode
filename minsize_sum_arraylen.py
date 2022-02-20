import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summm = 0
        w_start = 0
        currenlen = math.inf
        for i in range(len(nums)):

            summm += nums[i]
            while summm >= target:
                max_sum = i - w_start + 1
                currenlen = min(currenlen, max_sum)
                summm -= nums[w_start]
                w_start += 1
        if currenlen == math.inf:
            return 0
        return currenlen