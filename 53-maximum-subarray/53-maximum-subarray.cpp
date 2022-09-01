class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int maximumSum = nums[0];
        int tempSum = 0;
        
        for(int i=0; i<nums.size(); i++){
            if(tempSum<0) tempSum = 0;
            tempSum += nums[i];
            maximumSum = std::max(maximumSum, tempSum);
        }
        
        return maximumSum;
    }
};