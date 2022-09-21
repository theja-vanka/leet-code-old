// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1;
        int high = n;
        int middle;
        int correctVersion;
        while(low <= high){
            middle = low + (high - low)/2;
            if(!isBadVersion(middle)){
                low = middle + 1;
            }
            else{
                correctVersion = middle;
                high = middle - 1;  
            }
        }
        return correctVersion;
        
    }
};