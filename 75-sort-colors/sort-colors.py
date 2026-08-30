from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        index = 0
        for color in [0, 1, 2]:
            frequency = counts[color]
            for _ in range(frequency):
                nums[index] = color
                index += 1