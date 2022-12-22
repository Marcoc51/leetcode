class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''
        for char in s.lower():
            if char.isalnum():
                p += char
        end = -1
        for i in range(len(p) // 2):
            if p[i] != p[end]:
                return False
            end -= 1
        return True
