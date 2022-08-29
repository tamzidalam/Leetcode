class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        arr=[]
        i=1
        c=1
        if n % 2 ==0:
           
            while(c<n):
                
                arr.append(i)
                arr.append(-i)
                i+=1
                c+=2
        
        else:
            
            while(c<n):
                
                arr.append(i)
                arr.append(-i)
                i+=1
                c+=2
            
            arr.append(0)
                
                
       
        return arr
        
        
        