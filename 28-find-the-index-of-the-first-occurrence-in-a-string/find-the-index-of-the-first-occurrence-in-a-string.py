class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(needle)
        for i in range (0,len(haystack)):
            if needle in haystack[i:x]:
                return(i)
            else:
                x=x+1
                continue
        return(-1)