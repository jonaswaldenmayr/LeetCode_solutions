class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i,val in enumerate(digits):
            num += val *(10 ** (len(digits) - i -1))
        num += 1
        ret = []
        s = str(num)
        for i in s:
            ret.append(int(i))
        return(ret)
