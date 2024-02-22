class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result=[]
        
        
        maxxCandy=max(candies)
        
        
        for i in candies:
            if i+extraCandies >= maxxCandy:
                result.append(True)
            
            else:
                result.append(False)
        
        
        return result
        
        
        