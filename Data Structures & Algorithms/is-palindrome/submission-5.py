class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_char = "abcdefghijklmnopqrstuvwxyz1234567890"
        new_s = ""

        for c in s:
            if c.isalnum():
                new_s += c.lower()

        if new_s == new_s[::-1]:
            return True

        else: return False