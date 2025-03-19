#include <vector>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        
        // If all elements are already 1, return 0
        bool allOnes = true;
        for (int num : nums) {
            if (num == 0) {
                allOnes = false;
                break;
            }
        }
        if (allOnes) return 0;

        // If length is less than 3 and contains 0, it's impossible
        if (n < 3) return -1;

        int operations = 0;

        for (int i = 0; i <= n - 3; i++) {
            if (nums[i] == 0) { 
                // Flip next 3 elements
                nums[i] ^= 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                operations++;
            }
        }

        // Check if all elements are 1 after operations
        for (int num : nums) {
            if (num == 0) return -1;
        }

        return operations;
    }
};
