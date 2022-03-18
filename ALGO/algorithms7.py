"""
Valid Parentheses Problem:

Given a string containing just the characters '{','}','[',']', determine if the input string is valid.

An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

"""

class Solution:
    def isValid(self,s:str)->bool:
        stack=[]
        for c in s:
            if c=='(':
                stack.append('(')
            if c==')':
                if len(stack)==0:
                    return False
                if stack[-1]!='(':
                    return False
                else:
                    stack.pop()
            if c=='{':
                stack.append('{')
            if c=='}':
                if len(stack)==0:
                    return False
                if stack[-1]!='{':
                    return False
                else:
                    stack.pop()
            if c=='[':
                stack.append('[')
            if c==']':
                if len(stack)==0:
                    return False
                if stack[-1]!='[':
                    return False
                else:
                    stack.pop()
        if len(stack)>0:
            return False
        else:
            return True

