class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        mapp={}
        result=[]
        for i in range(len(names)):
            
            mapp[heights[i]] = names[i]
            
        
        l=len(mapp)
        
        i=0
        
        while i < l:
            temp=max(mapp)
            result.append(mapp[temp])
            del mapp[temp]
            i+=1
        
        return result
        
        
