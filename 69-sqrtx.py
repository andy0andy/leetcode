
"""
https://leetcode-cn.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:

        # pass
        # return int(math.sqrt(x))

        if x == 0 or x == 1:
            return x

        for i in range((x // 2)+1):
            if i ** 2 == x or (i ** 2 < x and (i+1) ** 2 > x):
                return i






if __name__ == "__main__":

    x = 2125209531

    res = Solution().mySqrt(x)
    print(res)




