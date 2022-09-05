class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_nums1 = {}
        hash_nums2 = {}
        hash_intersection = {}
        arr = []
        
        for num in nums1:
            if num in hash_nums1:
                hash_nums1[num] += 1
            else:
                hash_nums1[num] = 1
        
        for num in nums2:
            if num in hash_nums2:
                hash_nums2[num] += 1
            else:
                hash_nums2[num] = 1
        
        for key in hash_nums1.keys():
            if key in hash_nums2:
                hash_intersection[key] = min(hash_nums1[key], hash_nums2[key])
        
        for key, value in hash_intersection.items():
            arr += [key for x in range(value)]
        
        return arr