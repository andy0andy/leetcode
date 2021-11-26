from typing import List


"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
双指针法
"""



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if nums is None or len(nums) == 1:
            return len(nums)


        res, ind = 0, 1

        while ind < len(nums):

            if nums[res] == nums[ind]:
                ind += 1
            else:
                res += 1
                nums[res] = nums[ind]
                ind += 1

        return res+1




if __name__ == "__main__":

    nums = [1,1,2]

    res = Solution().removeDuplicates(nums)

    print(res)
