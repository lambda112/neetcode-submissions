class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_char = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = "".join(c for c in s.lower() if c in alpha_char)

        if s == s[::-1]:
            return True

        else: return False