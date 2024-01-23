class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        if n==0:
            return True 
            
            
        
        
        for i in range(0,len(flowerbed)):
            
            if flowerbed[i]==0:
                
                if i==0 and i==len(flowerbed)-1:
                    flowerbed[i]=1
                    n-=1
                if i==0 and i!=len(flowerbed)-1 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                
                if i!=0 and  i!= len(flowerbed)-1 and flowerbed[i-1] ==0 and flowerbed[i+1] == 0:
                    flowerbed[i]=1
                    n-=1
              
                
                if i==len(flowerbed)-1 and flowerbed[i-1] == 0:
                    flowerbed[i]=1
                    n-=1
            
                
        
        # print(flowerbed)
            
        
        if n<1:
            return True 
        return False
            