from typing import List

if __name__ == '__main__':
    # 寻找两个正序数组的中位数 （归并法）时间复杂度O(m+n)
    # def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    #     l1 = len(nums1)
    #     l2 = len(nums2)
    #     if l1 == 0 or l2 == 0:
    #         new = nums1 + nums2
    #         count = l1 + l2
    #         if count % 2 == 0:
    #             return (new[count // 2 - 1] + new[count // 2]) / 2
    #         else:
    #             return new[count // 2]
    #     new = []
    #     count, i, j = 0, 0, 0
    #     while count <= (l1 + l2) // 2:
    #         if i == l1:
    #             while j < l2:
    #                 new.append(nums2[j])
    #                 j += 1
    #                 count += 1
    #             break
    #         if j == l2:
    #             while i < l1:
    #                 new.append(nums1[i])
    #                 i += 1
    #                 count += 1
    #             break
    #         if nums1[i] < nums2[j]:
    #             new.append(nums1[i])
    #             i += 1
    #             count += 1
    #         else:
    #             new.append(nums2[j])
    #             j += 1
    #             count += 1
    #     print(new)
    #     print((l1 + l2) // 2)
    #     if (l1 + l2) % 2 == 0:
    #         a = new[-1]
    #         new.pop()
    #         b = new[-1]
    #
    #         return (a + b) / 2
    #     else:
    #         return new[-1]
    #
    # 寻找两个正序数组的中位数 （代码简化）时间复杂度O(m+n)
    # 只遍历一半。
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        length = (a + b) // 2
        # 两数组的下角标和遍历到的值与上一个值（合并奇偶）。
        cur, pre = -1, -1
        for _ in range(length + 1):
            pre = cur
            if nums1 and (not nums2 or nums1[0] < nums2[0]):
                cur = nums1[0]
                del (nums1[0])
            else:
                cur = nums2[0]
                del (nums2[0])
        if (a + b) % 2 == 0:
            return (pre + cur) / 2
        return cur


    nums1 = []
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
