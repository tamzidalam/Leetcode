class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        left=0
        right=0
        count=0
        
        i=0
        
        
        
        while(i<len(s)):
            
            if s[i]=='L':
                left+=1
            if s[i]=='R':
                right+=1
                
            if left == right:
                count+=1
            
            
            i+=1
        
       
        
        return count