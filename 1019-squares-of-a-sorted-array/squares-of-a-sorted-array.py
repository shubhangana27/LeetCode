class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        op=[]
        for i in nums:
            op.append(i*i)
        op.sort()
        return(op)