class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = ''
        T = max((numRows - 1) * 2, 1)
        for r in range(numRows):
            i = r
            while i < len(s):
                ret += s[i]
                i += T - (2*i % T)
        return ret