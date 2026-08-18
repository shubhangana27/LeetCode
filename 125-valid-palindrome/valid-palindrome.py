class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        punc=string.punctuation
        s = s.lower()
        s=s.replace(' ','')
        for i in s:
            if i in punc:
                s=s.replace(i,'')
        if s[::-1]==s:
            return(True)
        else:
            return(False)
