class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        
        hash_map = collections.defaultdict(int)
        
        for val in nums1:
            hash_map[val]+=1
        
        result= []
        
        for val in nums2:
            if hash_map[val]>0:
                result.append(val)
                hash_map[val]-=1
        return result
       
                
        