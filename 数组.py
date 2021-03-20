from typing import List
from sortedcontainers import SortedList

if __name__ == '__main__':
    # 数字跳跃，贪心 + 滑窗
    def jump(nums: List[int]) -> int:
        res, start, end = 0, 0, 1
        while end < len(nums):
            max_pos = 0
            for i in range(start, end):
                max_pos = max(max_pos, i + nums[i])
            start = end
            end = max_pos + 1
            res += 1
        return res
    print(jump([1, 2, 3]))
    # def generateMatrix(n: int) -> List[List[int]]:
    #     matrix = [[0] * n for _ in range(n)]
    #     num = 1
    #     left, right, top, bottom = 0, n - 1, 0, n - 1
    #     while left <= right and top <= bottom:
    #         for y in range(left, right + 1):
    #             matrix[top][y] = num
    #             num += 1
    #         for x in range(top + 1, bottom + 1):
    #             matrix[x][right] = num
    #             num += 1
    #         if left < right and top < bottom:
    #             for y in range(right - 1, left, -1):
    #                 matrix[bottom][y] = num
    #                 num += 1
    #             for x in range(bottom, top, -1):
    #                 matrix[x][left] = num
    #                 num += 1
    #         left += 1
    #         right -= 1
    #         top += 1
    #         bottom -= 1
    #
    #     return matrix
    # print(generateMatrix(3))
    #
    # # https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
    # # 子数组的差值不超过limit。 关键字： 子数组 -> 滑窗
    #
    # def longestSubarray(nums: List[int], limit: int) -> int:
    #     que = SortedList()
    #     left = res = 0
    #     for right, num in enumerate(nums):
    #         que.add(num)
    #         if que[-1] - que[0] > limit:
    #             que.remove(nums[left])
    #             left += 1
    #         res = max(res, right - left + 1)
    #     return res
    #
    #
    # nums = [10, 1, 2, 4, 7, 2]
    # limit = 5
    # print(longestSubarray(nums, limit))

    # def findMaxConsecutiveOnes(nums: List[int]) -> int:
    #     maxCount = 0
    #     start = end = -1
    #     for i, num in enumerate(nums):
    #         if num == 1 :
    #             if start == -1:
    #                 start = end = i
    #             else:
    #                 end = i
    #         else:
    #             if start != -1:
    #                 start = end = -1
    #         if end != -1 and end - start + 1 > maxCount:
    #             maxCount = end - start + 1
    #     return maxCount
    #
    # print(findMaxConsecutiveOnes([]))

    # # dic.value: (count, start, end)
    # def findShortestSubArray(nums: List[int]) -> int:
    #     dic = dict()
    #     for i, num in enumerate(nums):
    #         # 更新num的end
    #         if num in dic:
    #             dic[num][0] += 1
    #             dic[num][2] = i
    #         else:
    #             dic[num] = (1, i, i)
    #     maxNum = minLen = 0
    #     for count, start, end in dic:
    #         if maxNum < count:
    #             maxNum = count
    #             minLen = end - start + 1
    #         # 处理出现多个度相同的值
    #         elif maxNum == count:
    #             if minLen > (span := end - start + 1):
    #                 minLen = span
    #     return minLen
    #
    # nums = [1,2,2,3,1,4,2]
    # print(findShortestSubArray(nums))