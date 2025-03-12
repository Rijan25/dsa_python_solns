class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for x in range(numRows)]
        i = 0
        d = 1
        if numRows == 1:
            return s
        for char in s:
            ans[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        ret = ""
        for i in range(numRows):
            ret += "".join(ans[i])
        return ret
