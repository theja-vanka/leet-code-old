class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> crossnums;
        
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        int i = nums1.size() - 1;
        int j = nums2.size() - 1;
        
        while(i>=0 && j>=0){
            if(nums1[i] == nums2[j]){
                crossnums.push_back(nums1[i]);
                i -= 1;
                j -= 1;
            }
            else if(nums1[i] < nums2[j]){
                j -= 1;
            }
            else{
                i -= 1;
            }
        }
        
        return crossnums;
        }
};