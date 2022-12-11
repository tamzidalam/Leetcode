class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        mapp={}
        
        
        for i in arr:
            
            if i in mapp:
                mapp[i] +=1
             
            else:
                mapp[i]=1
        
        print(mapp)
       
        sett=set()
        
        for i in mapp.values():
            sett.add(i)
            
        if len(mapp) == len(sett):
            return True
        else:
            return False
                