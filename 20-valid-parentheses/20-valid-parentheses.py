class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        #hashmap with closing bracket as key and opening bracket as value
        closing = { ")" : "(", "]" : "[", "}" : "{" }
        
        for i in s:
            #if the character is a closing bracket, it would be in key
            if i in closing:
                #if the stack is not empty
                #and the last element of stack is opening bracket of same type
                if stack and stack[-1] == closing[i]:
                    stack.pop()
                    #pop the opening bracket from stack
                else:
                    return False
            else:
                #add opening bracket to stack
                stack.append(i)
        
        #valid brackets only if stack is empty
        return not stack
            