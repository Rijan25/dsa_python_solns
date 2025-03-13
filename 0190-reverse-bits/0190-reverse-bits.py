class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_num=0
        for i in range(32):
            reverse_num<<=1
            bit=n&1
            reverse_num=reverse_num|bit
            n>>=1
        return reverse_num

       


        