class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m = len(A)
        n = len(B)
        if m > n:
        	A, B, m, n = B, A, n, m
        if n == 0:
        	raise ValueError
        imin, imax = 0, m
        while imin <= imax:
        	i = (imin + imax) / 2
        	j = (m + n + 1) / 2 - i
        	if i < m and B[j-1] > A[i]:
        		imin = i + 1
        	elif i > 0 and A[i-1] > B[j]:
        		imax = i-1
        	else:
        		if i == 0:
        			max_of_left = B[j-1]
        		elif j == 0:
        			max_of_left = A[i-1]
        		else:
        			max_of_left = max(A[i-1],B[j-1])

        		if (m + n) % 2 == 1:
        			return max_of_left

        		if i == m:
        			min_of_right = B[j]
        		elif n == j:
        			min_of_right = A[i]
        		else:
        			min_of_right = min(A[i], B[j])
        		return (max_of_left + min_of_right) / 2.0

# if __name__ == '__main__':	
# 	sl = Solution()
# 	x1 = [1, 3]
# 	x2 = [2, 4]

# 	print(sl.findMedianSortedArrays(x1, x2))