""""
# 回溯模板
res = []
path = []

def backtrack(未探索区域, res, path):
    if 未探索区域满足结束条件:
        res.add(path) # 深度拷贝
        return
    for 选择 in 未探索区域当前可能的选择:
        if 当前选择符合要求:
            path.add(当前选择)
            backtrack(新的未探索区域, res, path)
            path.pop()

"""


isPalindrome = lambda a : s == s[::-1]
print(isPalindrome([1,2,1]))

from typing import List

# # 回溯：
# # 回溯的递归过程中会出现多个支线，在这些支线中会存在成功与失败，回溯要在出现失败的时候回溯到上一个状态。
# if __name__ == '__main__':
#
#     def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
#         res = newRes = []
#
#         def dfs(candidates: List[int], index, remain, value):
#             n = len(candidates)
#             if remain < 0:
#                 return
#             if remain == 0:
#                 res.append(sorted(value))
#                 return
#             for i in range(index + 1, n):
#                 dfs(candidates, i, remain - candidates[i], value + [candidates[i]])
#         dfs(candidates, 0, target, [])
#         return list(set([tuple(t) for t in res]))
#
#
#     candidates = [1]
#     target = 1
#     print(combinationSum2(candidates, target))
#
#     def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#
#         def dfs(candidates, index, remain, value):
#             n = len(candidates)
#             if remain < 0:
#                 return
#             if remain == 0:
#                 res.append(value)
#                 return
#             for i in range(index, n):
#                 if remain < 0:
#                     break
#                 dfs(candidates, i, remain - candidates[i], value + [candidates[i]])
#
#         dfs(candidates, 0, target, [])
#         return res
#
#
#     candidates = [1]
#     target = 1
#     print(combinationSum(candidates, target))
# def solveSudoku(board: List[List[str]]) -> None:
#     # 使用集合，方便移除已用数字。list的减法只有set()有效
#     nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
#     rows = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     blocks = [set() for _ in range(9)]
#     blanks = []
#     for i in range(9):
#         for j in range(9):
#             value = board[i][j]
#             bIndex = i // 3 * 3 + j // 3
#             if board[i][j] == '.':
#                 blanks.append((i, j))
#             else:
#                 rows[i].add(value)
#                 cols[j].add(value)
#                 blocks[bIndex].add(value)
#
#     # 将blanks一个个使用回溯法填入满足当前条件的数。
#     def backTrace(n):
#         # 遍历结束，此支线success。
#         if n == len(blanks):
#             return True
#         # 获取空缺的坐标
#         i, j = blanks[n]
#         bIndex = i // 3 * 3 + j // 3
#         # 获取(i, j)可以填入的数字rest
#         rest = nums - rows[i] - cols[j] - blocks[bIndex]
#         # rest为空时，表示当前空缺没办法填入数组，递归失败。
#         if not rest:
#             return False
#         # 逐个放入可填数字，并递归判断此支线的可行性。
#         for number in rest:
#             board[i][j] = number
#             rows[i].add(number)
#             cols[j].add(number)
#             blocks[bIndex].add(number)
#             # 递归进行验证下一可填数字。
#             if backTrace(n + 1):
#                 return True
#             rows[i].remove(number)
#             cols[j].remove(number)
#             blocks[bIndex].remove(number)
#     backTrace(0)
#
# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# solveSudoku(board)
# print(board)
