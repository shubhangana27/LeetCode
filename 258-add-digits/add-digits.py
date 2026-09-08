class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_num = 0
            for digit in str(num):
                sum_num += int(digit)
            num = sum_num
        return num
            