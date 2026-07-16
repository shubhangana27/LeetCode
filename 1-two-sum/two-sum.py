class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for j, num in enumerate(nums):
            complement=target-num
            if complement in num_map:
                return(num_map[complement],j)
            else:
                num_map[num]=j