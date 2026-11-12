class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mult = 1
        hasZero = False
        hasMultiZero = False
        for num in nums:
            if num == 0:
                if hasZero:
                    hasMultiZero = True
                hasZero = True
                continue
            mult = mult * num

        result = []
        for num in nums:
            if num == 0 and hasMultiZero:
                result.append(0)
            elif num == 0 and hasZero:
                result.append(mult)
            elif num != 0 and hasZero:
                result.append(0)
            elif num != 0 and not hasZero:
                result.append(mult // num)

        return result
