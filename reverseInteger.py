class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            r = int(str(x)[::-1])
        else:
            r = -int(str(abs(x))[::-1])
        if abs(r) > 2147483647:
            return 0
        else:
            return r