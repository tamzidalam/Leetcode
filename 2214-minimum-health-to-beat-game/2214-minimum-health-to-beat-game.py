class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        maxx=max(damage)
        
        for i in range(len(damage)):
            
            if  maxx == damage[i] :
                
                if maxx-armor < 1 :
                    damage[i] = 0
                
                else:
                    damage[i] = maxx-armor
                
                break
        
        
        return sum(damage)+1            
        