class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        
      
        mapp={}
        
        for i in arr:
            if i in mapp:
                mapp[i]+=1
            
            else:
                mapp[i]=1
            
        
        sett=set()
        
        for i in mapp.values():
            
            if i in sett:
                return False
            else:
                sett.add(i)
        
        
        return True 
    