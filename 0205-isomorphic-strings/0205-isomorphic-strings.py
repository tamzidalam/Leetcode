class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapST={}
        mapTS={}
        
        
        for i in range(len(s)):
            
            c1,c2=s[i],t[i]
            
            if s[i] in mapST:
                if mapST[s[i]] != c2:
                    return False
            
            mapST[s[i]]=c2
            
            
            if t[i] in mapTS:
                if mapTS[t[i]]!=c1:
                    return False 
            
            mapTS[t[i]]=c1
            
            
        
        return True
        
        
        
       