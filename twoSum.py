class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist = []
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if (nums[i] + nums[j] == target):
                    rlist.append(i)
                    rlist.append(j)
                    return rlist
                j = j + 1
            i = i + 1
    
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sl = Solution()
    result = sl.twoSum(nums, target)
    print (result)
