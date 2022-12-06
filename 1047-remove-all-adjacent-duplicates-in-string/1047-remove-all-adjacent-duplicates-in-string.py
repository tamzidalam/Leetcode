class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack=['']
        
        for i in range(0,len(s)):
            
            if len(s)!=0 and s[i] == stack[-1] :
                
                stack.pop()
             
            else:
                stack.append(s[i])
        
        
        return "".join(stack)
        
        
        
        