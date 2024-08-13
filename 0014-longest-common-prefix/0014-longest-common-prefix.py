class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        prefix=''
        min_length= float('inf')
        
        for s in strs:
            if len(s) < min_length:
                min_length=len(s)
        
        
        i=0
        
        while i<min_length:
            
            for j in strs:
                
                if strs[0][i]!=j[i]:
                    return prefix
                
            prefix+=j[i]
            
            i+=1
            
        return prefix