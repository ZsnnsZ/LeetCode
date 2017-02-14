class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
            
        sl = len(s)
        pl = len(p)
        t = [[False for _ in range(sl + 1)] for _ in range(pl + 1)]
        t[0][0] = True
        for i in range(2, pl + 1):
            t[i][0] = t[i - 2][0] and p[i - 1] == '*'
        for i in range(1, pl + 1):
            for j in range(1, sl + 1):
                if p[i - 1] != "*":
                    t[i][j] = t[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    t[i][j] = t[i - 2][j] or t[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        t[i][j] |= t[i][j - 1]

        return t[-1][-1]
