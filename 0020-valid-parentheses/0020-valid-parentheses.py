def balance(stack,o_b):
    if len(stack) == 0 :
        return False
    elif stack[-1] == o_b:
        stack.pop()
        return
    else:
        return False
        
class Solution:
    def isValid(self, s: str) -> bool:
        
        '''stack = []
        for i in s:
            if i in '(,[,{':
                stack.append(i)
            elif i == ')' :
                if len(stack) == 0:
                    return False
                
                elif stack[-1] == '(':
                    stack.pop()
                
                else:
                    return False
                
            elif i == ']':
                if len(stack) == 0:
                    return False 
                
                elif stack[-1] == '[':
                    stack.pop()
                    
                else:
                    return False
                    

            elif i == '}':
                if len(stack) == 0:
                    return False
                
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            False'''
        
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i == ')':
                if balance(stack,'(') == False:
                    return False
                    
            elif i == ']':
                if balance(stack,'[') == False:
                    return False
                
            elif i == '}':
                if balance(stack,'{') == False:
                    return False
                
        if stack:
            return False
        else:
            return True
                
        
                
        