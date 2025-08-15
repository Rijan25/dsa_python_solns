class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=''
        for item in digits:
            number+=str(item)
        number=int(number)+1
        return [int(x) for x in str(number).strip()]    
        