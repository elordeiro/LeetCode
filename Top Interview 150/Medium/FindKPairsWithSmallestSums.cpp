#include <iostream>
#include <vector>
#include <queue>
#include <set>

class Solution {
public:
    std::vector<std::vector<int>> kSmallestPairs(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        std::vector<std::vector<int>> sol;
        std::priority_queue<std::pair<int, std::pair<int, int>>, std::vector<std::pair<int, std::pair<int, int>>>, std::greater<std::pair<int, std::pair<int, int>>>> heap;
        
        for (int i = 0; i < k && i < len1; i++) {
            heap.push(std::make_pair(nums1[i] + nums2[0], std::make_pair(i, 0)));
        }
        
        while (k-- > 0 && !heap.empty()) {
            auto topElement = heap.top();
            int i = topElement.second.first;
            int j = topElement.second.second;
            heap.pop();
            sol.push_back({nums1[i], nums2[j]});
            
            if (++j < len2) {
                heap.push(std::make_pair(nums1[i] + nums2[j], std::make_pair(i, j)));
            }
        }
        
        return sol;
    }
};


int main () {
    Solution sol;
    std::vector<int> nums1{1,2,4};
    std::vector<int> nums2{-1,1,2};
    int k = 10;
    std::vector<std::vector<int>> result = sol.kSmallestPairs(nums1, nums2, k);
    
    std::cout << "[ ";
    for (const auto& r : result) {
        int i, j;
        i = r[0];
        j = r[1];
        std::cout << "(" << i << ", " << j << ") ";
    }
    std::cout << "]" << std::endl;
}