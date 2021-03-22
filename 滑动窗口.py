import bisect
import collections
from itertools import accumulate
from typing import List

if __name__ == '__main__':

    def maxValue( n: int, index: int, maxSum: int) -> int:
        res = 1
        left, right = index, index
        # 初始化数组后的剩余数
        rest = maxSum - n
        # 当两个指针均到达边界，可以直接计算能分配多少，不必一步一步计算浪费时间
        while left > 0 or right < n - 1:
            # 左右指针的区间即是每一轮分配的个数（每一位均分配1）
            span = right - left + 1
            if rest >= span:
                # 存货充沛，直接分配,指针向两边移动
                res += 1
                rest -= span
                # 指针移动到边界时，不再移动
                left = left - 1 if left > 0 else 0
                right = right + 1 if right < n - 1 else n - 1
            else:
                # 存货不够了，可以直接的答案，不必继续
                break
        res += rest // n
        return res
    print(maxValue(6,1,10))
    # def longestSubstring(s: str, k: int) -> int:
    #     res = left = right = 0
    #     while right < len(s):
    #         if s[right] != s[left]:
    #             if right - left >= k:
    #                 res += right - left
    #             left = right
    #         right += 1
    #     if right - left >= k:
    #         res += right - left
    #     return res
    #
    #
    # s = "ababbc"
    # k = 2
    # print(longestSubstring(s, k))

    # K连续位的最小翻转次数（困难） https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/
    # def minKBitFlips(self, A: List[int], K: int) -> int:
    #     N = len(A)
    #     que = collections.deque()
    #     res = 0
    #     for i in range(N):
    #         if que and i >= que[0] + K:
    #             que.popleft()
    #         if len(que) % 2 == A[i]:
    #             if i +  K > N: return -1
    #             que.append(i)
    #             res += 1
    #     return res

    # 滑窗 字典。python使用counter  https://leetcode-cn.com/problems/permutation-in-string/submissions/
    # 使用字典可以忽略字符先后顺序
    # def checkInclusion(s1: str, s2: str) -> bool:
    #     # 统计s1中各字符出现次数
    #     counter1 = collections.Counter(s1)
    #     left, right = 0, len(s1) - 1
    #     # right此时没包括入内
    #     counter2 = collections.Counter(s2[left: right])
    #     while right < len(s2):
    #         # 加入right
    #         counter2[s2[right]] += 1
    #         if counter1 == counter2:
    #             return True
    #         # 将left 次数减一
    #         counter2[s2[left]] -= 1
    #         if counter2[s2[left]] == 0:
    #             del counter2[s2[left]]
    #
    #         left += 1
    #         right += 1
    #     return False
    #
    #
    #
    # s1 = "adc"
    # s2 = "dcda"
    # print(checkInclusion(s1, s2))

    # def subarraysWithKDistinct(A: List[int], K: int) -> int:
    #     n = len(A)
    #     # for left in range(n):
    #     #     right
    #     print(A[1:2])
    #
    #
    # A = [1, 2, 1, 3, 4]
    # K = 3
    # print(subarraysWithKDistinct(A, K))
    # def maxTurbulenceSize(arr: List[int]) -> int:
    #     res, n = 2, len(arr)
    #     if n < 3:
    #         return n
    #     count = res
    #     for mid in range(1, n - 1):
    #         left, right = mid - 1, mid + 1
    #         if arr[left] > arr[mid] < arr[right] or arr[left] < arr[mid] > arr[right]:
    #             count += 1
    #         else:
    #             res = max(res, count)
    #             count = 2
    #     res = max(res, count)
    #     return res
    # arr = [0,8,45,88,48,68,28,55,17,24]
    # print(maxTurbulenceSize(arr))

    # 可获得的最大值https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/submissions/
    # 由只能从首位拿取可以推得剩下的n - k 个数必然是连续最小值。
    # 即找到最小连续数之和可找到最大值
    # def maxScore(cardPoints: List[int], k: int) -> int:
    #     n = len(cardPoints)
    #     # 滑窗大小 n - k
    #     winSize = n - k
    #     s =sum(cardPoints[:winSize])
    #     mi = s
    #     for start in range(winSize, n):
    #         s += cardPoints[start] - cardPoints[start - winSize]
    #         mi = min(mi, s)
    #     return sum(cardPoints) - mi
    #
    # cardPoints = [96,90,41,82,39,74,64,50,30]
    # k = 8
    # print(maxScore(cardPoints, k))

    # def equalSubstring(s: str, t: str, maxCost: int) -> int:
    #     n = len(s)
    #     # 计算s,t对应字母ascii码差值。并将结果累加(accumulate)
    #     accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
    #     maxLength = 0
    #
    #     for i in range(1, n + 1):
    #         #
    #         start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
    #         maxLength = max(maxLength, i - start)
    #
    #     return maxLength
    #
    # s = "abcd"
    # t = "bcdf"
    # cost = 3
    # print(equalSubstring(s, t, cost))
    # def characterReplacement(s: str, k: int) -> int:
    #     n = len(s)
    #     dic = {}
    #     left = res = 0
    #     for right in range(n):
    #         # 统计字母出现次数
    #         # dic.get(s[right], 0) 当dic中没有对应建，赋默认值0
    #         dic[s[right]] = dic.get(s[right], 0) + 1
    #         # 获取字典最值对应键 方法二： max(dic, key= dic.get)
    #         maxLetter = max(dic, key=lambda x: dic[x])
    #         # 将出现次数最大字母作为目标字幕，其余为待替换字母。
    #         # 待替换字母数大于k时，左边界右缩,原左边界字母出现次数减一，更新最大出现次数字母
    #         while right - left + 1 - dic[maxLetter] > k:
    #             dic[s[left]] -= 1
    #             left += 1
    #             maxLetter = max(dic, key=lambda x: dic[x])
    #         res = max(res, right - left + 1)
    #     return res
    #
    #
    # s = "ABAA"
    # k = 0
    # print(characterReplacement(s, k))
