class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        temp=0
        maxx=-999999999
        for i in range(0,k):
            temp+=nums[i]
        
        maxx=max(temp,maxx)
        i=k
        j=0
        print(i)
        while(i<len(nums)):
            
            temp+=nums[i]-nums[j]
            maxx=max(temp,maxx)
            
            i+=1
            j+=1
        print(maxx)  
        return maxx/k
            
            
            
            
            