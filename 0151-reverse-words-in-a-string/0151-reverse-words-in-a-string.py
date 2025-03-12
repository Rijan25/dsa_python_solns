class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()[::-1]
        reversed_sentence=' '.join(words)
        return reversed_sentence    
        

        