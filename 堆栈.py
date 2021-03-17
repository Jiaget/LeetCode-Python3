if __name__ == '__main__':
    def isValidSerialization( preorder: str) -> bool:
        token = '*'
        stack = [token]
        preorder = preorder.split(',')

        for e in preorder:
            if e.isdigit():
                if stack:
                    stack.pop()
                    stack.append(token)
                    stack.append(token)
                else:
                    return False
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
    print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    # def calculate(s: str) -> int:
    #     num = 0
    #     op = '+'
    #     stack = []
    #     for i, e in enumerate(s) :
    #         if e.isdigit():
    #             num = num * 10 + int(e)
    #         # 遍历到最后或者运算符时，代表数字取完
    #         if i == len(s) - 1 or e in '+-*/':
    #             if op == '+':
    #                 stack.append(num)
    #             if op == '-':
    #                 stack.append(-num)
    #             if op == '*':
    #                 stack.append(stack.pop() * num)
    #             if op == '/':
    #                 # 除法的取整需要对正负进行讨论
    #                 top = stack.pop()
    #                 if top < 0:
    #                     stack.append(int(top / num))
    #                 else:
    #                     stack.append(top // num)
    #             num = 0
    #             op = e
    #     return sum(stack)
    # print(calculate("14-3/2"))

    # def calculate(s: str) -> int:
    #     res, num, sign = 0, 0, 1
    #     stack = []
    #     for c in s:
    #         if c.isdigit():
    #             num = 10 * num + int(c)
    #         elif c == "+" or c == "-":
    #             res += sign * num
    #             num = 0
    #             sign = 1 if c == "+" else -1
    #         elif c == "(":
    #             stack.append(res)
    #             stack.append(sign)
    #             res = 0
    #             sign = 1
    #         elif c == ")":
    #             res += sign * num
    #             num = 0
    #             res *= stack.pop()
    #             res += stack.pop()
    #     res += sign * num
    #     return res
    #
    # s = "2147483647"
    # print(calculate(s))
