from typing import List

if __name__ == '__main__':
    # 升级，四数和.就是三数和再套一层
    def fourSum(nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        res = []
        for i in range(n - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                right, left = n - 1, j + 1
                while left < right:
                    s = nums[i] + nums[j] + nums[right] + nums[left]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                    else:
                        if s > target:
                            right -= 1
                        else:
                            left += 1
        return res


    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(fourSum(nums, target))
     # # 暴力
    # def threeSum(nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     if n < 3:
    #         return []
    #     nums.sort()
    #     res = []
    #     for i in range(n):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         right, left = n - 1, i + 1
    #         while left < right:
    #             if nums[i] + nums[left] + nums[right] == 0:
    #                 res.append([nums[i], nums[left], nums[right]])
    #             while left < right and nums[right] == nums[right - 1]:
    #                 right -= 1
    #             while left < right and nums[left] == nums[left + 1]:
    #                 left += 1
    #             else:
    #                 if nums[i] + nums[left] + nums[right] > 0:
    #                     right -= 1
    #                 else:
    #                     left += 1
    #     return res

    # def threeSumClosest(nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     res = nums[0] + nums[1] + nums[2]
    #     for i in range(n - 2):
    #         left, right = i + 1, n - 1
    #         while left < right:
    #             if abs(nums[i] + nums[left] + nums[right] - target) < abs(res - target):
    #                 res = nums[i] + nums[left] + nums[right]
    #             left += 1
    #             right -= 1
    #     return res
    # nums = [-1,2,1,2,-4]
    # print(threeSumClosest(nums, -6))
