from typing import List
import heapq

if __name__ == '__main__':
    # 性能优化：1. 不要使用排序，使用最小堆heapq
    #         2. 订单数为0要及时出栈，不要占据空间浪费性能。
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        bqueue = []
        squeue = []
        for price, amount, typ in orders:
            # 采购订单
            if typ == 0:
                while squeue and amount > 0 and squeue[0][0] <= price:
                    temp = squeue[0][1] # 最小销售价格的订单笔数
                    squeue[0][1] -= amount
                    if squeue[0][1] <= 0:
                        heappop(squeue)
                    amount -= temp
                if amount > 0: # 若采购单任然未完成
                    heappush(bqueue, [-price, amount])
            if typ == 1:
                while bqueue and amount > 0 and abs(bqueue[0][0]) >= price:
                    temp = bqueue[0][1]
                    bqueue[0][1] -= amount
                    if bqueue[0][1] <= 0:
                        heappop(bqueue)
                    amount -= temp
                if amount > 0:
                    heappush(squeue, [price, amount])
        res = 0

        for buy in bqueue:
            res += buy[1]
        for sell in squeue:
            res += sell[1]
        return res % (10**9 + 7)

    # def evalRPN(tokens: List[str]) -> int:
    #     stack = []
    #     for token in tokens:
    #         if token not in '+-*/':
    #             stack.append(int(token))
    #         else:
    #             b, a = stack.pop(), stack.pop()
    #             if token == '+':
    #                 stack.append(a + b)
    #             elif token == '-':
    #                 stack.append(a - b)
    #             elif token == '*':
    #                 stack.append(a * b)
    #             elif token == '/':
    #                 stack.append(int(a / b))
    #     return stack.pop()
    #
    # print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

    # def isValidSerialization( preorder: str) -> bool:
    #     token = '*'
    #     stack = [token]
    #     preorder = preorder.split(',')
    #
    #     for e in preorder:
    #         if e.isdigit():
    #             if stack:
    #                 stack.pop()
    #                 stack.append(token)
    #                 stack.append(token)
    #             else:
    #                 return False
    #         else:
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 return False
    #     if stack:
    #         return False
    #     return True
    # print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
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
