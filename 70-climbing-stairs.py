
"""
https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        lst = [0, 1, 2]

        for i in range(3, n+1):

            lst.append(lst[-2] + lst[-1])


        return lst[n]





if __name__ == "__main__":

    n = 38
    res = Solution().climbStairs(n)

    print(res)


