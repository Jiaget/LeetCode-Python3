from typing import List


class Status():
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum, self.rSum, self.mSum, self.iSum = lSum, rSum, mSum, iSum


if __name__ == '__main__':

    # 2.分治（线段树）
    # lSum 表示[l, r][l, r]内以ll为左端点的最大子段和
    # rSum表示[l, r][l, r]内以rr为右端点的最大子段和
    # mSum表示[l, r][l, r]内的最大子段和
    # iSum表示[l, r][l, r]的区间和
    def maxSubArray(nums: List[int]) -> int:
        return get(nums, 0, len(nums) - 1).mSum


    def pushUp(l: Status, r: Status) -> Status:
        iSum = l.iSum + r.iSum
        lSum = max(l.lSum, r.lSum + l.iSum)
        rSum = max(r.rSum, r.iSum + l.rSum)
        # 最大字段和可能跨越左右区间，也可能不。
        mSum = max(max(r.mSum, l.mSum), l.rSum + r.lSum)
        return Status(lSum, rSum, mSum, iSum)


    def get(nums, l, r) -> Status:
        if l == r:
            return Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) >> 1  # 整除2
        # 分治
        lSub = get(nums, l, m)
        rSub = get(nums, m + 1, r)
        # 合并
        return pushUp(lSub, rSub)

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))

    # 1.动态规划
    # [-2,1,-3,4,-1,2,1,-5,4]
    # 寻找最大子序的结尾比较困难，因为不清楚负数的后面会不会有更大的正数
    # 因此先确定子序的结尾来找子序的开头。
    # 每次遍历的nums[i],可以得到以他为结尾的子序的最大和f(i)
    # 状态转移方程:
    # f(i) = max( f(i - 1) + nums[i], nums[i])
    # # max中左边代表子序加上当前元素的值，右边代表舍弃先前子序，当前元素作为新子序。
    # def maxSubArray(nums: List[int]) -> int:
    #     # nums[0]之前没有子序列，故f(i - 1)=pre=0
    #     pre, maxN = 0, nums[0]
    #     for num in nums:
    #         # 状态转移方程
    #         pre = max(pre + num, num)
    #         # 取最大值
    #         maxN = max(pre, maxN)
    #     return maxN
