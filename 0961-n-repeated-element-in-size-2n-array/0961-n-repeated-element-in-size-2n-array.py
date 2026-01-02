import collections
class Solution(object):
    def repeatedNTimes(self, nums):
        count=collections.Counter(nums)
        n=len(list(set(nums)))
        for i in count:
            if count[i]==n-1:
                return i