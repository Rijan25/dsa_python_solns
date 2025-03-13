class Solution:
    def countBits(self, n: int) -> List[int]:
        out=[]
        while n>=0:
            nobits=bin(n).count('1')
            n-=1
            out.append(nobits)
        return out[::-1]
        