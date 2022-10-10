class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
            
        dicS={}
        
        for i in s:
            
            if i in dicS:
                dicS[i] +=1
            
            else:
                dicS[i]=1
        
        for i in t:
            if i in dicS:
                dicS[i] -=1
                
                if dicS[i] == 0:
                    dicS.pop(i)
            else:
                return False
        
        
        if len(dicS) == 0:
            return True
        return False
        