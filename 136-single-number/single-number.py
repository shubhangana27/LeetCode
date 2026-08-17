from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts=Counter(nums)
        first_unique = next((num for num in nums if counts[num] == 1), None)
        return first_unique
        