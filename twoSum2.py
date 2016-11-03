class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 9
    Solution = Solution()
    print(Solution.twoSum(nums, target))
