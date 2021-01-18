from typing import List

if __name__ == '__main__':
    # 括号生成 DFS
    def generateParenthesis(n: int) -> List[str]:
        init = ['(']
        # count代表匹配的括号对数。remain代表剩余的左括号个数
        count, remain = 0, 1
        res = []

        def generateBrackets(a, count, remain):
            if count == n and remain == 0:
                res.append("".join(a))
            else:
                # 递归层数到达2*n时不满足括号匹配，退出
                if len(a) == 2 * n:
                    return
                if count <= n and remain > -1:
                    a.append('(')
                    generateBrackets(a, count, remain + 1)
                    a.pop()
                    a.append(')')
                    generateBrackets(a, count + 1, remain - 1)
                    a.pop()

        generateBrackets(init, count, remain)
        return res


    print(generateParenthesis(3))

    # # 括号匹配
    # def isValid(s: str) -> bool:
    #     brackets = {'(': ')', '[': ']', '{': '}'}
    #     leftBrackets = "([{"
    #     stack = []
    #     for bracket in s:
    #         if bracket in leftBrackets:
    #             stack.append(bracket)
    #         else:
    #             if brackets[stack.pop(-1)] == bracket:
    #                 continue
    #             else:
    #                 return False
    #     return True

    # s = "([])"
    # print(isValid(s))
