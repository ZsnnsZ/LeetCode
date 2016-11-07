class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s
        b = a[-1::-1]
        start, end, maxl = 0, 0, 0
        for i in range(len(a)):
            start = i
            j = 0
            while j < len(a) and i < len(a):
                if a[i] == b[j]:
                    j += 1
                    i += 1
                    end = i
                else:
                    j += 1
                    i = start
            if (end - start) > maxl:
                maxl = end - start
                ts = a[start:end]
        return ts

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        dp = [1] * len(s)
        center = 0
        for i, _ in enumerate(s):
            if dp[center] + center > i:
                dp[i] = min(dp[2*center-i], dp[center]+center-i) 
            while i - dp[i] >= 0 and i + dp[i] < len(s) and s[i-dp[i]] == s[i+dp[i]]:
                dp[i] += 1
            if dp[i] > dp[center]:
                center = i
        return s[center-dp[center]+2:center+dp[center]:2]

public String longestPalindrome(String s) {
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}