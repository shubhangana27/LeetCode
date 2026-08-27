class Solution:
    def reverseVowels(self, s: str) -> str:
        x = set("aeiouAEIOU")
        y=list(s)
        left,right=0,len(s)-1
        while left<right:
            if y[left] in x and y[right] in x:
                y[left],y[right]=y[right],y[left]
                left=left+1
                right=right-1
            elif y[left] in x:
                right=right-1
            elif y[right] in x:
                left=left+1
            else:
                left=left+1
                right=right-1
        return "".join(y)