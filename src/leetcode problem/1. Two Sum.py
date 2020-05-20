# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 0:
            return nums
        map = dict()
        for i, x in enumerate(nums):
            if (target - x) in map:
                return [i, map[target - x]]
            map[x] = i

# Testcase
# foo = Solution()
# result = foo.twoSum([2, 7, 11, 18], 13)
# print(result)

# Tips
# map is a dict type, IN operation judges key rather than value
# bar = {2: 0, 7: 1}
# 0 in bar      False
# 2 in bar      True
# 1 in bar      False
# 7 in bar      True