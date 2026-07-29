class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_s=0
        max_current=0
        for i in s:
            if i ==" ":
                max_current=0
            else:
                max_current=max_current+1
                max_s=max_current
        return (max(max_s,max_current))
