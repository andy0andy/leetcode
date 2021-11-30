from typing import List

"""
https://leetcode-cn.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        ans = -1

        for i in range(len(nums)):

            if nums[i] == target:
                ans = i
                break
            elif i == 0 and nums[i] > target:
                ans = 0
                break
            elif nums[i] < target:
                ans = i+1
            elif nums[i] > target:
                break

        return ans



if __name__ == "__main__":

    nums = [1,3,5,6]
    target = 0

    res = Solution().searchInsert(nums, target)

    print(res)


