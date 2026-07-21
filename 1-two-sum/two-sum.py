class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range (len(nums)):
            complement=target-nums[i]
            if complement in nums and nums.index(complement)!=i:
                l.append(i)
                l.append(nums.index(complement))
                break
        return l