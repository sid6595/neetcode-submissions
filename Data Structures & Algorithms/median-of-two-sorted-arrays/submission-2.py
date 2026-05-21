class Solution:
    def get_kth(self, arr_1, len_a1, arr_2, len_a2, k, a_start: int = 0, b_start: int = 0):
        if len_a1 > len_a2:
            return self.get_kth(arr_2, len_a2, arr_1, len_a1, k, b_start, a_start)
        
        if len_a1 == 0:
            return arr_2[b_start + k - 1]
        
        if k == 1:
            return min(arr_1[a_start], arr_2[b_start])
         
        i = min(len_a1, k // 2)
        j = min(len_a2, k // 2)

        if arr_1[a_start + i - 1] > arr_2[b_start + j - 1]:
            return self.get_kth(arr_1, len_a1, arr_2, len_a2 - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(arr_1, len_a1 - i, arr_2, len_a2, k - i, a_start + i, b_start)




    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2 
        right = (len(nums1) + len(nums2) + 2) // 2

        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left)
         + self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
        