class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        num = abs(x)
        reversed_num = 0

        while num != 0:
            digit = num % 10              # pull out the last digit
            reversed_num = reversed_num * 10 + digit   # build the reversed number
            num = num // 10                # remove that digit from num

        reversed_num *= sign               # reattach the original sign

        # Check signed 32-bit integer range: [-2^31, 2^31 - 1]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num
       
        