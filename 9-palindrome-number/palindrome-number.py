class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        left=0
        right=len(n)-1
        while left<right:
            if n[left]==n[right]:
                left=left+1
                right=right-1
                continue
            return False
        return True

