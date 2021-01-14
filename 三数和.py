from typing import List

if __name__ == '__main__':
    # 暴力
    def threeSum(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right, left = n - 1, i + 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                else:
                    if nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return res


    nums = [-2,0,1,1,2]
    print(threeSum(nums))
