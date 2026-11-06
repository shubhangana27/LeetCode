class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        l=0
        for i in range (0,len(nums)):
            if val!=nums[i]:
                nums[k]=nums[i]
                k=k+1
            else:
                l=l+1
        return k