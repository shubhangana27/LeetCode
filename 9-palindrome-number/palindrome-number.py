class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        rev=0
        while a>0:
            d=a%10
            a=a//10
            rev=rev*10+d
        if rev==x:
            return True
        else:
            return False

