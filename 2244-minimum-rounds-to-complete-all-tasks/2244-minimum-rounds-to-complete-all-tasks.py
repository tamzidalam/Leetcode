class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        hashMap={}
        
        for i in tasks:
            if i in hashMap:
                hashMap[i] +=1
                
            else:
                hashMap[i]=1
            
            
        count=0
        for i in hashMap.values():
            if i < 2 :
                return -1
            elif i % 3 == 0:
                count+=i//3
            else:
                count+=(i//3)+1
                
        return count 