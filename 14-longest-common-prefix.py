from typing import List


"""
https://leetcode-cn.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        if len(strs) == 0:
            return ""

        min_str = min(strs)
        max_str = max(strs)

        for i, v in enumerate(min_str):

            if v != max_str[i]:
                res = min_str[:i]
                return res

        return min_str



if __name__ == "__main__":

        strs = ["ab","a"]

        res = Solution().longestCommonPrefix(strs)
        print(res)