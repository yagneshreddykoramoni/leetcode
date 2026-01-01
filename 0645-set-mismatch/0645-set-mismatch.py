import collections
class Solution(object):
    def findErrorNums(self, nums):
        count = collections.Counter(nums)
        dup=0
        mis=0
        for i in range(1,len(nums)+1):
            if count[i]==2:
                dup=i
            elif count[i]==0:
                mis=i
        return [dup,mis]