class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        st=""
        for i in range (0,len(s)):
            current=s[i]
            if current not in st:
                st=st+current
                max_len=max(max_len,len(st))
            else:
                st = st[st.index(current) + 1:]
                st += current

        return(max_len)