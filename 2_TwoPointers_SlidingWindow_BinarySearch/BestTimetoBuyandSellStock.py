class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mx = 0
        l = 0
        r = l + 1

        while l < r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l

            if prices[l] <= prices[r]:
                mx = max(mx, prices[r] - prices[l])
                r += 1

        return mx
