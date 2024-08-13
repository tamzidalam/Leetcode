class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        symbols={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        
        total=0
        
        for i in range(0,len(s)-1):
            if symbols[s[i]]<symbols[s[i+1]]:
                total-=symbols[s[i]]
            else:
                total+=symbols[s[i]]
        
        total+=symbols[s[len(s)-1]]
        
        return total
        