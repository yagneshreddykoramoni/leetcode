class Solution(object):
    def lengthOfLastWord(self, s):
        a=0
        b=0
        s = list(s)
        s.reverse()
        for i in range(len(s)):
            if s[i]==" " and b==1:
                break
            elif s[i]==" ":
                continue
            else:
                a+=1
                b=1
        return a