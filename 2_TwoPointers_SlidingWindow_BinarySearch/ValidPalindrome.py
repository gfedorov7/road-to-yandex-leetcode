class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "qwertyuiopasdfghjklzxcvbnm1234567890"

        s = s.lower()
        s = s.replace(' ', '')

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] not in alphabet:
                l += 1
                continue
            elif s[r] not in alphabet:
                r -= 1
                continue

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
