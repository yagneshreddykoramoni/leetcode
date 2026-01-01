class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=0
        b=0
        for i in nums:
            if i==1:
                a+=1
            else:
                if a>b:
                    b=a
                a=0
        if a>b:
            b=a
        return b
        