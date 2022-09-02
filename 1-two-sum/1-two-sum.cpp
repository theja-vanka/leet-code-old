class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> diffTarget;
        vector<int> returnValue = {-1, -1};
        
        for(int i=0; i<nums.size(); i++){
            
            map<int,int>::iterator it = diffTarget.find(nums[i]);
            if(it != diffTarget.end())
            {
                returnValue = {it->second, i};
                return returnValue;
            }
            
            diffTarget[target-nums[i]] =  i;
        
        }
        return returnValue;
    }
};