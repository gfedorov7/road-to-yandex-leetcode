class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        mx = 0
        while l < r:
            mx = max(mx, self.calculateArea(height, l, r))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mx

    def calculateArea(self, height, i1, i2):
        mn = min(height[i1], height[i2])
        return (i2 - i1) * mn

s = Solution()
print(s.maxArea([1,1]))