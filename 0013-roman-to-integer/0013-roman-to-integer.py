class Solution(object):
    def romanToInt(self, s):
        a = []
        for i in range(len(s)):
            if(s[i]=='I'):
                a.append(1)
            elif(s[i]=='V'):
                a.append(5)
            elif(s[i]=='X'):
                a.append(10)
            elif(s[i]=='L'):
                a.append(50)
            elif(s[i]=='C'):
                a.append(100)
            elif(s[i]=='D'):
                a.append(500)
            elif(s[i]=='M'):
                a.append(1000)
        s=0
        for i in range(len(a)-1):
            if(a[i]>=a[i+1]):
                s+=a[i]
            else:
                s-=a[i]
        s+=a[-1]
        return s
        
        