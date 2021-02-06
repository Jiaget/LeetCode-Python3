import bisect
from itertools import accumulate
from typing import List

if __name__ == '__main__':
    # 可获得的最大值https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/submissions/
    # 由只能从首位拿取可以推得剩下的n - k 个数必然是连续最小值。
    # 即找到最小连续数之和可找到最大值
    def maxScore(cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # 滑窗大小 n - k
        winSize = n - k
        s =sum(cardPoints[:winSize])
        mi = s
        for start in range(winSize, n):
            s += cardPoints[start] - cardPoints[start - winSize]
            mi = min(mi, s)
        return sum(cardPoints) - mi

    cardPoints = [96,90,41,82,39,74,64,50,30]
    k = 8
    print(maxScore(cardPoints, k))

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
