class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        
        costs.sort()
        
        summ=0
        
        number=0
        
        for i in costs:
            summ+=i
            if summ > coins:
                return number
        
        
            number+=1
        
        
        return number 
        
        
        
        