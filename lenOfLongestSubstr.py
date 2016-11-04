class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        orgmax = 0
        newmax = 0
        for i in range(len(s)):
            if s[i] not in s[left:i]:
                orgmax += 1
            else:
                newleft = s[left:i].index(s[i]) + 1
                left += newleft
                orgmax = orgmax - newleft + 1
            newmax = max(orgmax,newmax)
        return newmax

# if __name__ == '__main__':
# 	s = 'asdasd'
# 	sl = Solution()
# 	print(sl.lengthOfLongestSubstring(s))