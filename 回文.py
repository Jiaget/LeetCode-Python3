from typing import List

if __name__ == '__main__':
    # 中心扩散，将每个元素作为回文中心，判断回文长度，取最长
    def spreadCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


    def longestPalindrome(s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            # 回文长度为奇数
            l1, r1 = spreadCenter(s, i, i)
            # 回文长度为偶数
            l2, r2 = spreadCenter(s, i, i + 1)
            if r1 - l1 > right - left:
                left, right = l1, r1
            if r2 - l2 > right - left:
                left, right = l2, r2
        return s[left: right + 1]


    # # 双指针向中间聚拢，遇到两个字母相同的，判定两字母中间是否构成回文。
    # # 嵌套了三层循环（估计第三层循环增加了右指针的移动，时间复杂度应该是O(n3)而非O（n2））
    # # 效率和暴力差不太多。
    # def longestPalindrome(s: str) -> str:
    #     res = ""
    #     n = len(s)
    #     ml, mr = -1, -1
    #     for left in range(n - 1):
    #         right = n - 1
    #         while left < right:
    #             i, j = left, right
    #             while i <= j and s[i] == s[j]:
    #                 if (i == j or i + 1 == j) and (right - left + 1) > (mr - ml + 1):
    #                     ml = left
    #                     mr = right
    #                 i += 1
    #                 j -= 1
    #             right -= 1
    #     return s[ml, mr + 1]

    str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(longestPalindrome(str))
