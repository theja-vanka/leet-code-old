class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        int length = nums.size();
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<length-1; i++){
            
            if(nums[i]==nums[i+1]){
                return true;
            }
            
        }
        
        return false;
    }    
};