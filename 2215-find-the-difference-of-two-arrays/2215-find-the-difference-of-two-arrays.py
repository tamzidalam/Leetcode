class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        hash1=set()
        for i in nums1:
            hash1.add(i)
            
        hash2=set() 
        for i in nums2:
            hash2.add(i)
         
        print(hash1)
        arra=[]
        
        temp=[]
        
        for i in hash1:
            if i not in hash2:
                temp.append(i)
         
        arra.append(temp)
        
        temp=[]
        for i in hash2:
            if i not in hash1:
                temp.append(i)
         
        arra.append(temp)
        
        
        return arra