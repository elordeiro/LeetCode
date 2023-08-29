#include <iostream>
#include <chrono>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        int left  = 0;
        int right = nums.size() - 1;
        int start = -1;

        while (left <= right) {
            int mid = (left + right) >> 1;
            int mid_el = nums[mid];
            if (target < mid_el)
                right = mid - 1;
            else if (target > mid_el)
                left = mid + 1;
            else {
                start = mid;
                right = mid - 1;
            }
        }

        if (start == -1)
            return {-1, -1};
        
        int end = -1;
        left = start;
        right = nums.size() - 1;
        
        while (left <= right) {
            int mid = (left + right) >> 1;
            int mid_el = nums[mid];
            if (target < mid_el)
                right = mid - 1;
            else if (target == mid_el) {
                end = mid;
                left = mid + 1;
            }
            else
                left = mid + 1;
        }

        return {start, end};
    }
};


int main () {
    Solution sol = Solution();
    std::vector nums = {1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10};
    int target = 10;
    auto start_time = std::chrono::high_resolution_clock::now();
    std::vector<int> res = sol.searchRange(nums, target);
    std::cout << "[" << res[0] << ", " << res[1] << "]" << std::endl;
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    std::cout << "Runtime: " << elapsed_time.count() << std::endl;
}