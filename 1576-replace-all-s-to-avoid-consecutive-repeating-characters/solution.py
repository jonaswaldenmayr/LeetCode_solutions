class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        corr = 97

        for i,l in enumerate(s):
            if l != "?":
                continue
            left = s[i-1] if i > 0 else None
            right = s[i+1] if i < len(s)-1 else None
            if right == "?":
                right = None

            m = 0
            while True:
                cand = chr(corr +m)
                if cand != left and cand != right:
                    s[i] = cand
                    break
                m += 1

        return "".join(s)
