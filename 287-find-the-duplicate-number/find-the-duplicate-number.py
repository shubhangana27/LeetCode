class Solution:
    from collections import Counter
    def findDuplicate(self, nums: list[int]) -> int:
        counts=Counter(nums)
        max_element=counts.most_common(1)[0][0]
        return max_element