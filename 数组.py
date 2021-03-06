from typing import List
from sortedcontainers import SortedList

if __name__ == '__main__':
    # https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
    # 子数组的差值不超过limit。 关键字： 子数组 -> 滑窗

    def longestSubarray(nums: List[int], limit: int) -> int:
        que = SortedList()
        left = res = 0
        for right, num in enumerate(nums):
            que.add(num)
            if que[-1] - que[0] > limit:
                que.remove(nums[left])
                left += 1
            res = max(res, right - left + 1)
        return res


    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(longestSubarray(nums, limit))

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