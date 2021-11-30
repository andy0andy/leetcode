
"""
https://leetcode-cn.com/problems/add-binary/
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # print(str(bin(int(a, 2) + int(b, 2))))
        return str(self.ttob(self.btot(int(a)) + self.btot(int(b))))


    def btot(self, b: int) -> int:
        # 二进制转十进制

        t = 0
        b = str(b)

        for i in range(len(b)):
            t += int(b[len(b) - 1 - i]) * pow(2, i)

        return t

    def ttob(self, t: int) -> int:
        # 十进制转二进制

        b = []

        while t > 1:
            b.append(t % 2)
            t = t // 2

        if t == 1:
            b.append(t)

        if t == 0:
            b.append(0)

        return int("".join(list(map(str, (reversed(b))))))



if __name__ == "__main__":
    a, b = "0", "0"

    res = Solution().addBinary(a, b)

    print(res)

