class Solution(object):
    def removeElement(self, nums, val):
        l = []
        j = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                l.append(nums[i])
                nums[j]=nums[i]
                j+=1
            else:
                continue
        nums = nums[:j]
        return len(nums)
        