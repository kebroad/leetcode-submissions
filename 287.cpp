#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution{
public:
    int findDuplicate(vector<int>& nums){
        sort(nums.begin(), nums.end());
        for(int i = 1; i < nums.size(); i++){
            if(nums[i-1] == nums[i]){
                return nums[i-1];
            }
        }
        return -1;
    }
};


int main(){
vector<int> nums  = {1,2,2,3,4,5};
Solution s;  
int a = s.findDuplicate(nums);
a++;
}

