

"""
https://leetcode-cn.com/problems/implement-strstr/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)



if __name__ == "__main__":

    haystack, needle = "aaaaa", "bba"

    res = Solution().strStr(haystack, needle)

    print(res)



