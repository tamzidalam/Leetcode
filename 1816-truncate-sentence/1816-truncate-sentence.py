class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        result=""
        
        for i in s:
            
            if i==' ':
                                
                k-=1
                
                if k==0:
                    break
                    
                result+=" "
            
            else:
                result+=i
        
        return result
                
                
                
        