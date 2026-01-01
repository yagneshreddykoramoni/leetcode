class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        b=[]
        for i in nums:
            a=0
            for j in nums:
                if j<i:
                    a+=1
            b.append(a)
        return b
        