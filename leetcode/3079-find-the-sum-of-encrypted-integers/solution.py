class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            s = str(x)
            m = max(s)
            total += int(m * len(s))
        return total
