class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high){
            int middle = low + (high - low)/2;
            if(nums[middle] == target){
                return middle;
            }
            else if (nums[middle] > target){
                high = middle - 1;
            }
            else{
                low = middle + 1;
            }
        }
        return -1;
    }
};