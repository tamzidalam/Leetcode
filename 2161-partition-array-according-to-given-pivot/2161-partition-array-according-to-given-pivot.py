class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        before=[]
        after=[]
        flag=0
        for i in nums:
            if i < pivot:
                before.append(i)
            
            elif i == pivot:
                
                after.insert(0,i)
            
            else:
                after.append(i)
                
        
        before+=after
        
        return before