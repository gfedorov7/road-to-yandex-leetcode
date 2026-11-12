class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length

        l = 0
        r = 1

        count = 1
        mx = 0
        while r < length:
            if s[r] not in s[l:r]:
                count += 1
                r += 1
                mx = max(mx, count)
            else:
                l += 1
                r = l + 1
                mx = max(mx, count)
                count = 1

        return mx
