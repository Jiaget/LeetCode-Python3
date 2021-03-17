from typing import List

if __name__ == '__main__':
    # 动规矩阵 https://leetcode-cn.com/problems/distinct-subsequences/submissions/
    # 行t,列s
    # s[i] == t[j]: dp[i - 1][j - 1] + dp[i - 1][j] // dp[i - 1][j] 表示t[j]历史匹配次数， dp[i - 1][j - 1] 表示t[j]之前字母匹配成功次数。两次累加代表t[:j]目前匹配的次数
    # s[i] != t[j]: dp[i - 1][j]  //当前匹配失败，继承历史即可
    def numDistinct(s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]

    # # 按摩师问题。创建二维动规矩阵
    # # dp[i][0] 代表第i天不接受的最大时长
    # # dp[i][1] 代表第i天接受的最大时长
    # def massage(nums: List[int]) -> int:
    #     dp = [[0] * 2 for _ in range(len(nums))]
    #     for i in range(len(nums)):
    #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    #         dp[i][1] = dp[i - 1][0] + nums[i]
    #     return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])
    #
    # nums = [1, 2, 3, 1]
    # print(massage(nums))
    #
    # # 最小花费爬楼梯。和按摩师解法类似，这次使用一维dp，需要前面两个数的值
    # # 状态转移方程 ：
    # # f(i) = min(f(i - 1), f(i - 2)) + f(i)
    # # 跨上第i阶台阶可能从上一阶跨过来，也可能由上上阶跨级过来。取最小值即可
    # # 至于第i阶跨不跨，是下一阶思考的问题。
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     n = len(cost)
    #     if n < 3:
    #         return min(cost)
    #     for i in range(2, n):
    #         cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
    #     # 最后一步可能从倒数第二阶跨过，也可能从最后一阶跨过。取最小即可
    #     return min(cost[n - 1], cost[n - 2])