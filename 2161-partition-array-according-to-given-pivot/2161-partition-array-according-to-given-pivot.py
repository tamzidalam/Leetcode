class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        ans=[]
        
        for i in nums:
            if i < pivot:
                ans.append(i)
        
        l=len(ans)
        for i in nums:
            if i>pivot:
                ans.append(i)
            
            elif i == pivot:
                ans.insert(l,i)
                
        
        return ans