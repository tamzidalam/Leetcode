class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
    
#         last=m+n-1
        
#         while m >0 and n>0:
#             if nums1[m]>nums2[n]:
#                 print('hello')
#                 nums1[last] = nums1[m]
#                 m-=1
            
#             else:
#                 print('hello')
#                 nums1[last] = nums2[n]
#                 n-=1
            
#             last-=1
        
#         while second>0:
#             nums1[last]=nums2[n]
#             last-=1
#             n-=1