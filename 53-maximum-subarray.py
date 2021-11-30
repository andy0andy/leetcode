from typing import List

"""
https://leetcode-cn.com/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):

            if (nums[i] + nums[i-1]) > nums[i]:
                nums[i] += nums[i-1]


        return max(nums)





if __name__ == "__main__":

    nums = [-2,1,-3,4,-1,2,1,-5,4]

    ans = Solution().maxSubArray(nums)

    print(ans)



