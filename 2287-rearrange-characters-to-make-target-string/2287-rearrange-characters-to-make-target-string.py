class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        S=Counter(s)
        tr=Counter(target)
        count=inf
        
        for i in tr:
            
            if i not in S:
                return 0 
            else:
                count = min(count, S[i]//tr[i])
                
        
        return count