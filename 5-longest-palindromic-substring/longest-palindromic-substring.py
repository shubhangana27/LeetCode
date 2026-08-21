class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        result_length=0
        for i in range (len(s)):
            # odd length string
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > result_length:
                    result=s[l:r+1]
                    result_length=r-l+1
                l=l-1
                r=r+1
            
            # even length string 
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > result_length:
                    result=s[l:r+1]
                    result_length=r-l+1
                l=l-1
                r=r+1
        return result