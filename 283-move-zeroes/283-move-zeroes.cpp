class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>::iterator it;
        vector<int> zeroLocation = {};
        
        for(int i=0; i<nums.size(); i++){
             if(nums[i] == 0){
                 zeroLocation.push_back(i);
             }
        }
        for(int i=zeroLocation.size()-1; i>=0; i--){
            it=nums.begin()+zeroLocation[i];
            nums.erase(it);
            nums.push_back(0);
        }
    }
};