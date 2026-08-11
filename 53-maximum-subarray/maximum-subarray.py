class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        sum_x=nums[0]
        for i in range (1,len(nums)):
            sum_x= max(nums[i]+sum_x,nums[i])
            max_sum=max(sum_x,max_sum)
        return(max_sum) 