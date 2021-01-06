import collections
import heapq
import sys
from typing import List


class ListNode(object):
    def __init__(self, val=0, pnext=None):
        self.val = val
        self.next = pnext


if __name__ == '__main__':
    # 整数反转以及溢出判断
    def reverse(x: int) -> int:
        symbol, res = 1, 0
        if x < 0:
            symbol = -1
            x = -x
        while x != 0:
            tmp = x % 10
            newRes = res * 10 + tmp
            if (newRes - tmp) // 10 != res:
                return 0
            res = newRes
            x = x // 10
        return res * symbol
    print(reverse(-12312))
    # # z字转换
    # def convert(s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #     # 最后将numRows个字符串拼接在一起即可
    #     res = ["" for _ in range(numRows)]
    #     # 1正序，-1逆序。 res数组每次遍历到0或者numRows时反向
    #     i, turn = 0, -1
    #     for e in s:
    #         res[i] += s
    #         if i == 0 or i == numRows - 1:
    #             turn = -turn
    #         i += turn
    #     return "".join(res)
    # sys.maxsize


    # def largeGroupPositions(s: str) -> List[List[int]]:
    #     i, start, end = 0, 0, 0
    #     res = list()
    #     while i < len(s) - 2:
    #         if s[i] == s[i + 1] and s[i] == s[i + 2]:
    #             start = i
    #             i += 3
    #             while i < len(s) and s[i] == s[i - 1]:
    #                 i += 1
    #             end = i - 1
    #             res.append([start, end])
    #         else:
    #             i += 1
    #     return res
    # s = "abbxxxxzzy"
    # print(largeGroupPositions(s))

    # def fib(n: int) -> int:
    #     if n < 2:
    #         return n
    #     a, b = 0, 1
    #     for i in range(2, n + 1):
    #         temp = b
    #         b = a + b
    #         a = temp
    #     return b
    # print(fib(4))
    # 滑动窗口最大值（优化） 单调队列 使用双端队列deque实现。
    # # 使用双端队列是为了1.当队首不在窗口内，弹出。2.在队尾添加元素时，将队尾较小得元素弹出。
    # def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #     # 该队列只存下角标
    #     q = collections.deque()
    #     # 将第一个窗口的元素塞入单调队列
    #     for i in range(k):
    #         # 保证队列元素从大到小排列，并且舍去较小得元素。
    #         while q and nums[i] >= nums[q[-1]]:
    #             q.pop()
    #         q.append(i)
    #     res = [nums[q[0]]]
    #     for i in range(k, len(nums)):
    #         while q[-1] <= i - k:
    #             q.popleft()
    #         while q and nums[i] >= nums[q[-1]]:
    #             q.pop()
    #         q.append(i)
    #         res.append(nums[q[0]])
    #     return res
    # nums = []
    # k = 0
    # print(maxSlidingWindow(nums, k))
   # # 滑动窗口最大值 （使用优先队列队列） 优先队列是一种自动排列队列。使用自带heapq实现
    # def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #     length = len(nums)
    #     # 由于heapq是小顶堆，进行相反数处理。存入值和下角标，判断队内元素在原数组的位置
    #     q = [(-nums[i], i) for i in range(k)]
    #     heapq.heapify(q)
    #     res = [-q[0][0]]
    #     for i in range(k, length):
    #         heapq.heappush(q, (-nums[i], i))
    #         # 如果队首下角标超过窗口左半边，出队
    #         while i - k > q[0][1]:
    #             heapq.heappop(q)
    #         res.append(-q[0][0])
    #     return res
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3
    # print(maxSlidingWindow(nums, k))
    # # 滑动窗口最大值 for循环里用了max 时间复杂度O（mn）。果然超时
    # def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #     mList = []
    #     for i in range(len(nums) - k + 1):
    #         list = nums[i:(i + k)]
    #         if list:
    #             mList.append(max(list))
    #     return mList

    # 花坛 小技巧：前后补充0，避免边界
    # def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    #     counter = 0
    #     flowerbed = [0] + flowerbed + [0]
    #     print(flowerbed)
    #     for i in range(1, len(flowerbed) - 1):
    #         if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
    #             counter += 1
    #             flowerbed[i] = 1
    #     if n <= counter:
    #         return True
    #     else:
    #         return False
    #
    #
    # flowerbed = [1, 0]
    # n = 1
    # print(canPlaceFlowers(flowerbed, n))

    # 最长递增子序列
    # def lengthOfLIS(nums: List[int]) -> int:
    #     tails, res = [0] * len(nums), 0
    #     for num in nums:
    #         i, j = 0, res
    #         while i < j:
    #             m = (i + j) // 2
    #             if tails[m] <= num:
    #                 i = m + 1
    #             else:
    #                 j = m
    #         tails[i] = num
    #         if j == res: res += 1
    #     return res
    #
    # nums = [1,3,6,7,9,4,10,5,6]
    # print(lengthOfLIS(nums))

    # 无重叠区间
    # def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    #     length = len(intervals)
    #     if length == 0: return 0
    #     intervals.sort(key=lambda x: x[1])
    #     # 设定第一个右边界
    #     right = intervals[0][1]
    #     count = 0
    #     for i in range(1, length):
    #         # 左边界比上一个区间的右边界小，说明重叠
    #         if intervals[i][0] < right:
    #             count += 1
    #         else:
    #             # 重新设置一个右边界
    #             right =intervals[i][1]
    #     return count
    # intervals = [[1, 2], [1, 2], [1, 2]]
    # print(eraseOverlapIntervals(intervals))
    # python 实现最大堆
    # # 最后一块石头的重量 学习python的最小堆调库
    # def lastStoneWeight(stones: List[int]) -> int:
    #     stones = [-stone for stone in stones]
    #     heapq.heapify(stones)
    #     while len(stones) > 1:
    #         x, y = heapq.heappop(stones), heapq.heappop(stones)
    #         if x != y:
    #             heapq.heappush(stones, x - y)
    #     if stones: return -stones[0]
    #     return 0
    # print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
    # 补齐数组.
    # def minPatches(nums: List[int], n: int) -> int:
    #     right, count, i = 1, 0, 0
    #     # 永远从[0,1）开始扩展区间
    #     while right <= n:
    #         # 数组在区间内，则不需要添加数，并扩充区间
    #         if i < len(nums) and nums[i] <= right:
    #             right += nums[i]
    #             i += 1
    #         else:
    #             # 定义的区间出现空缺，将right作为补充，区间翻倍
    #             right = right * 2
    #             count += 1
    #     return count
    # nums = [1,2,2]
    # n = 5
    # print(minPatches(nums, n))

    # # 股票系列，leetcode188。动态规划 2维dp table。
    # # dp[i][j]: i代表天数，j代表状态：
    # # j=0: 不操作。 j=1(奇数)：买入状态。j=2(偶数)：卖出状态
    # # 买入状态可以是当天买入，也可以是延续前一天的买入状态：
    # # 举例 dp[i][1] = dp[i-1][0] - prices[i] 当天买入即 前一天的余额减去当天的价格
    # # dp[i][1] = dp[i-1][1]  延续则直接继承前一天的买入时的余额
    # # 卖出状态可以是当天卖出，也可以是延续前一天的卖出状态：
    # # dp[i][2] = dp[i-1][1] + prices[i]
    # # dp[i][2] = dp[i-1][2]
    # # 两种状态都取最大的可能情况->max()
    # # j的范围为2k+1。因为k笔交易代表会有2k+1种状态。
    # # dp[i][j]的值为当前金钱数，买入时减去交易额，卖出加上交易额。比如第一次买入时值为负数。
    # def maxProfit(k: int, prices: List[int]) -> int:
    #     n = len(prices)
    #     if n <= 1:
    #         return 0
    #     dp = [[0] * (2 * k + 1) for _ in range(n)]
    #     # 第0天时，只会有买入操作，不会有卖出操作。故而第0天的j为偶数时为0
    #     j = 1
    #     while j < 2 * k:
    #         dp[0][j] = -prices[0]
    #         j += 2
    #     # 从第一天开始，j + 1代表买入状态，j + 2代表卖出状态。
    #     # 每种状态都需要前一天的不同状态取最大值。
    #     for i in range(1, n):
    #         j = 0
    #         while j < 2 * k - 1:
    #             dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
    #             dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
    #             j += 2
    #     # 最后返回矩阵的最后一位值，整个矩阵也保留了计算的全部过程
    #     return dp[n - 1][2 * k]
    #
    # # 单调栈的应用 每日温度。预测多久温度升高，预测方向单调，因而联想到单调栈
    # def dailyTemperatures(T: List[int]) -> List[int]:
    #     length = len(T)
    #     res = [0]*length
    #     stack = list()
    #     for i in range(len(T)):
    #         while stack and T[stack[-1]] < T[i]:
    #             cur = stack[-1]
    #             stack.pop()
    #             res[cur] = i - cur
    #         stack.append(i)
    #     return res

    # 接雨水问题，可以联想到括号配对.用栈。几个特殊情况（2，1，3）.（2，1，0，1，3）
    # # 单调栈
    # def trap(height: List[int]) -> int:
    #     ans = 0
    #     stack = list()
    #     for i in range(len(height)):
    #         while stack and height[i] > height[stack[-1]]:  # 当后柱大于栈顶柱时出栈
    #             # 取栈顶前两元素形成三柱，判断存水状况。无法取两个元素时，清栈退出。
    #             mid = stack[-1]
    #             stack.pop()
    #             if not stack:
    #                 break
    #             l = stack[-1]
    #             r = i
    #             h = min(height[l], height[r]) - height[mid]  # 取左右两柱最小高度和中间柱高的差作为储水高度
    #             ans += (r - l - 1) * h
    #         stack.append(i)
    #     return ans

    # # 柱状图面积的应用，矩阵最大面积。服用柱状图面积代码. 这部分顺便学习python3简单处理矩阵吧。
    # def maximalRectangle(matrix: List[List[str]]) -> int:
    #     row = len(matrix)  # 共l行
    #     if row == 0:
    #         return 0
    #     col = len(matrix[0])
    #     heights = [0] * col
    #     area = 0
    #     # 每一行都会复用heights列表。每一行的每一列上的“1”会和上一行进行叠加形成矩形。
    #     # 没遍历一行都会将该行计算的矩形长度列表传递给 [柱状图最大面积]函数中。取每一行的最大值即可
    #     for i in range(row):
    #         for j in range(col):
    #             if matrix[i][j] == "0":
    #                 heights[j] = 0
    #             else:
    #                 heights[j] += 1
    #         area = max(area, largestRectangleArea(heights))
    #     return area
    #
    # # 柱状图面积 单调栈解法使用哨兵缩短代码。在heights首位增加一个高度为0的元素，不必判断栈空的特殊情况。
    # def largestRectangleArea(heights: List[int]) -> int:
    #     length = len(heights)
    #     if len == 0:
    #         return 0
    #     if len == 1:
    #         return heights[0]
    #     l = [0]
    #     heights = l + heights + l
    #     length += 2
    #     area = 0
    #     stack = list()
    #     stack.append(0)
    #     for i in range(length):
    #         if i != 0:
    #             while stack and heights[stack[-1]] > heights[i]:
    #                 height = heights[stack[-1]]
    #                 stack.pop()
    #                 width = i - stack[-1] - 1
    #                 area = max(width * height, area)
    #             stack.append(i)
    #     return area

    # 柱状图面积 单调栈解法（优化前）
    # def largestRectangleArea(heights: List[int]) -> int:
    #     length = len(heights)
    #     if len == 0:
    #         return 0
    #     if len == 1:
    #         return heights[0]
    #     area = 0
    #     stack = list()
    #     for i in range(length):
    #         while stack and heights[stack[-1]] >= heights[i]:
    #             height = heights[stack[-1]]
    #             stack.pop()
    #             width = 0
    #             if stack:  # 栈非空时说明先前栈顶的矩形之前有比之矮的矩形，宽度不能向左扩展，只能向右扩展至i
    #                 width = i - stack[-1] - 1  # 之前获取的栈顶元素已被移除，这里补减一个1
    #             else:
    #                 width = i  # 栈空时说明i左侧的矩形中，先前栈顶矩形最矮，该矩形的宽左右均可扩展
    #             area = max(width * height, area)
    #         stack.append(i)
    #         # 清空栈
    #     while stack:
    #         height = heights[stack[-1]]
    #         stack.pop()
    #         if stack:
    #             width = length - stack[-1] - 1
    #         else:
    #             width = length
    #         area = max(width * height, area)
    #     print(stack)
    #     return area

    # # 柱状图面积暴力解法 (绝对超时，主要是理清题目思路) https://leetcode-cn.com/problems/largest-rectangle-in-histogram/ （hard）
    # def largestRectangleArea(heights: List[int]) -> int:
    #     width = 1
    #     max_area = 0
    #     for index, h in enumerate(heights):
    #         i = index
    #        当前柱的左右方向边各自遍历，直到高度比自己矮无法形成矩形 或者out of index
    #         while i > 0 and heights[i - 1] >= h:
    #             width += 1
    #             i -= 1
    #         i = index
    #         while i < len(heights)-1 and heights[i + 1] >= h:
    #             width += 1
    #             i += 1
    #         max_area = max(max_area, width * h)
    #         width = 1
    #     return max_area

    # 窗口 def lengthOfLongestSubstring(s: str) -> int:
    #     temp = set()
    #     p = count = 0
    #     n = len(s)
    #     for i in range(n):  # i是左指针，代表窗口的左边框
    #         if i != 0:
    #             temp.remove(s[i-1])
    #         while p < n and s[p] not in temp:
    #             temp.add(s[p])
    #             p += 1
    #         count = max(count, p - i)
    #     return count
    #
    #
    # str = "pwwkew"
    # res = lengthOfLongestSubstring(str)
    # print(res)

    # 1
    # def removeDuplicateLetters(s: str) -> str:
    #     stack = []
    #     counter = collections.Counter(s)
    #     for c in s:
    #         counter[c] -= 1
    #         if c not in stack:
    #             while stack and c < stack[-1] and counter[stack[-1]] > 0:
    #                 stack.pop()
    #             stack.append(c)
    #     return ''.join(stack)

    # 2
    # def firstUniqChar(s: str) -> int:
    #     counter = collections.Counter(s)
    #
    #     for i, c in enumerate(s):
    #         if counter[c] == 1:
    #             return i
    #     return -1
    # print(firstUniqChar("abacb"))

# 3链表
# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     resultNode = ListNode(0)
#     c = 0  # 进位符
#     cur = resultNode  # 指针
#     while l1 or l2:
#         # 将短链表后面补0
#         temp1 = l1.val if l1 else 0
#         temp2 = l2.val if l2 else 0
#         result = temp1 + temp2 + c
#         c = result // 10  # 取进位
#         cur.next = ListNode(result % 10)  # 取个位数创建链表
#         cur = cur.next
#         if l1:
#             l1 = l1.next
#         if l2:
#             l2 = l2.next
#     if c > 0:
#         cur.next = ListNode(c)  # 为最后一位的进位创建链表
#     return resultNode.next
# Node1 = ListNode(0)
# c1 = Node1
# c1.next = ListNode(5)
# c1.next.next = ListNode(5)
#
# Node2 = ListNode(0)
# c2 = Node2
# c2.next = ListNode(2)
# c2.next.next = ListNode(3)
# result = addTwoNumbers(c1.next, c2.next)
# print(result.val, result.next.val)
