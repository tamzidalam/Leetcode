class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        
        dic={}
        for i in range(len(paths)):
            dic[paths[i][1]]=paths[i][0]
            
        print(dic)
        
        for i in dic:
            
            if i not in dic.values():
                return i
            