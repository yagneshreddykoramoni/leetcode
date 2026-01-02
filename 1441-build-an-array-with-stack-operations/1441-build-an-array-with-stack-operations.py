class Solution(object):
    def buildArray(self, target, n):
        s=[]
        ans=[]
        i=0
        j=1
        while j<=n:
            ans.append("Push")
            s.append(j)
            if s[i]!=target[i]:
                ans.append("Pop")
                s=s[:i]
                i-=1
            if s==target:
                break
            i+=1
            j+=1
        return ans