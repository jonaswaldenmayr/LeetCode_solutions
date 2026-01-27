class Solution:
    def isPalindrome(self, x: int) -> bool:
        if  not isinstance(x, int):
            return False
        s = str(x)

        l, r = 0, len(s)-1
        while l<=r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1

        return True
