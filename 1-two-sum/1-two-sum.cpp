class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> diffTarget;
        vector<int> returnValue;
        
        for(int i=0; i<nums.size(); i++){
            
            map<int,int>::iterator it = diffTarget.find(nums[i]);
            if(it != diffTarget.end())
            {
                returnValue = {it->second, i};
                return returnValue;
            }
            
            diffTarget.insert(pair<int, int>(target-nums[i], i));
        
        }
        return returnValue;
    }
};