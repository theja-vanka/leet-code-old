class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>::iterator it;
        for(int i=nums.size()-1; i>=0; i--){
            if(nums[i] == 0){
                it=nums.begin()+i;
                nums.erase(it);
                nums.push_back(0);    
            } 
        }
    }
};