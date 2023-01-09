class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        postive=[]
        negative=[]
        
        for i in nums:
            
            if i > 0 :
                postive.append(i)
            else:
                negative.append(i)
                
       
        result=[]
        
        j=0
        
        while j<len(postive):
            result.append(postive[j])
            result.append(negative[j])
            j+=1
        
        return result            