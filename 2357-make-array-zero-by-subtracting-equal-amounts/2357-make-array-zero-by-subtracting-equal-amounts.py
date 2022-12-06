class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        hashmap={}
        count=0
        
        for i in nums:
            
            if i != 0 and i not in hashmap :
                hashmap[i]=i
                count+=1
                
        
        return count