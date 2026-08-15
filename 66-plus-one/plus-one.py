class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        for i in digits:
            x=x+str(i)
        y=1+int(x)
        l=[]
        for i in str(y):
            l.append(int(i))
        return (l)