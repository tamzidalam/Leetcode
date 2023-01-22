class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1=nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v2=vec
        ans=0
        print(v2.v1)
        for i in range(len(v2.v1)):
            ans+=self.v1[i]*v2.v1[i]
        
        return ans
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)