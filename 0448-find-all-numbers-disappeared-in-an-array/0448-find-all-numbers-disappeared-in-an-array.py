class Solution(object):
    def findDisappearedNumbers(self, nums):
        a=[]
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                a.append(i)
        return a
        