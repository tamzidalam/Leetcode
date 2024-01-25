class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        
        for i in range(0,len(s)):
            
            if s[i]==' ':
                                
                k-=1
                
                if k==0:
                    return s[:i]
                    
            
           
        return s
    
    
    #Time Complexity
                
                
                
        