class Solution(object):
    def isValid(self, s):
        '''
        stack=[]
        for i in range(len(s)):
            if(s[i]=='('):
                stack.append('(')
            elif(s[i]=='['):
                stack.append('[')
            elif(s[i]=='{'):
                stack.append('{')
            elif(s[i]==')'):
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
                    break
            elif(s[i]==']'):
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
                    break
            elif(s[i]=='}'):
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
                    break
        else:
            if len(stack)==0:
                return True
            else:
                return False
        '''
        a = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1]!=a[char]:
                    return False
                    break
                else:
                    stack.pop()
        else:
            if not stack:
                return True
            else:
                return False