class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            if num in idxs and idxs[num] != idx:
                return [idxs[num], idx]
            idxs[target - num] = idx

        return []
