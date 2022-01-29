class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        conSet=set()
        
        for i in nums:
            conSet.add(i)
            
        
        print(conSet)
        
        total=0
        
        for i in conSet:
            count=1
            if i-1 not in conSet:
                while i+1 in conSet:
                    count+=1
                    i+=1
                
                if count>total:
                    total=count
        
        
        return total