class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        l=0
        for l in range (0,len(nums)):
            if val!=nums[l]:
                nums[k]=nums[l]
                k=k+1
            else:
                l=l+1
        return(k)
