class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # negative numbers
            return False
        elif x < 10: # 0~9
            return True
        elif x % 10 == 0: # numbers end with 0
            return False
        n = 0
        while x > n: # only compare half of x, reducing the expense
            n = n*10 + x%10
            x = x // 10
        return x == n or x == n // 10 # one for even numbers and another for odd numbers