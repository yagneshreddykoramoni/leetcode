class Solution(object):
    def plusOne(self, digits):
        a=''
        for i in digits:
           a+=str(i)
        a=int(a)
        a+=1
        a=str(a)
        b=[]
        for i in a:
            b.append(int(i))
        return b
        