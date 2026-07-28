class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        m=""
        for i in range (len(n)-1,-1,-1):
            m=m+n[i]
        if m==n:
            return True
        else:
            return False
