class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        import math
        count=0
        for i in range (len(nums)):
            x=math.log10(nums[i])
            y=floor(x)+1
            if y%2==0:
                count+=1
        return (count)