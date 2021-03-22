import heapq


class Solution:
    # 字符串相加
    def addStr(self, num1, num2):
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        res = []
        while i >= 0 or j >= 0 or carry != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            s = x + y + carry
            carry = s // 10
            res.append(str(s % 10))
            i -= 1
            j -= 1
        return "".join(res[::-1])

    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = "0"
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            x = int(num1[i])
            # 事先确定位数，避免之后补0
            toAdd = ['0'] * (n1 - i - 1)
            for j in range(len(num2) - 1, -1, -1):
                y = int(num2[j])
                # 按位相乘，并补上进位
                xy = x * y + carry
                # 处理进位
                toAdd.append(str(xy % 10))
                carry = xy // 10
            # 补上最后一位的进位
            if carry > 0:
                toAdd.append(str(carry))
            toAdd = "".join(toAdd[::-1])
            res = self.addStr(res, toAdd)
        return res

solution = Solution()
num1 = "2"
num2 = "3"
print(solution.multiply(num1, num2))
