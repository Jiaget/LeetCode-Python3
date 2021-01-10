from typing import List

if __name__ == '__main__':
    def rotate(nums: List[int], k: int) -> None:
        if not nums:
            return
        for _ in range(k):
            nums.insert(0, nums.pop(-1))
        return
    nums = []
    k = 3
    rotate(nums, k)
    print(nums)