class Solution:
    def longestCommonPrefix(self, A: List[str]) -> str:
        
        
        output=""
        
        index=0
        
        for i in A[0]:
            
            for k in range(1,len(A)):
                
                if( index >= len(A[k]) or i != A[k][index] ):
                    return output
            
            output+=i
            index+=1
                    
        
        return output       