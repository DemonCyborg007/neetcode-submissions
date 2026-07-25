class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            print(i)
            if i == '(' :
                stack.append(i)
            elif i == '{' :
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack)==0:
                    return False
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if len(stack)==0:
                    return False
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
                
            elif i == ']':
                if len(stack)==0:
                    return False
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
                
        print(stack)
        if len(stack)==0:
            return True
        else:
            return False