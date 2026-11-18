class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums):
            num = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    result.append([num, nums[l], nums[r]])

                if total <= 0:
                    l += 1
                else:
                    r -= 1

                while total <= 0 < l < len(nums) - 1 and nums[l - 1] == nums[l]:
                    l += 1

                while total >= 0 and 0 < r < len(nums) - 1 and nums[r] == nums[r+1]:
                    r -= 1

            i += 1
            while 0 < i < (len(nums) - 1) and nums[i-1] == nums[i]:
                i += 1

        return result
