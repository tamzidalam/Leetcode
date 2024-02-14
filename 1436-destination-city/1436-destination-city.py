class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        
        destSet=set()
        
        
        for i in range(len(paths)):
            
            destSet.add(paths[i][0])
            
        
        print(destSet)
        
        for i in range(len(paths)):
            
            destination=paths[i][1]
            
            if destination not in destSet:
                return destination
            
