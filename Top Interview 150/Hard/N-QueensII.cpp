#include <unordered_set>
#include <vector>
#include <iostream>
#include <chrono>
#include <numeric>

class Solution{
    int res;
    int n;
    std::vector<int> cols;
    std::vector<int> neg_diagonal;
    std::vector<int> pos_diagonal;
    std::vector<int> unassigned_cols;

public:
    int totalNQueens(int x) {
        res = 0;
        n = x;
        cols.resize(n);
        neg_diagonal.resize(n * 2);
        pos_diagonal.resize(n * 2);
        unassigned_cols.resize(n);
        std::iota(unassigned_cols.begin(), unassigned_cols.end(), 0);
        
        backtrack(0);
        return res;
    }

private:
    void backtrack(int row) {
        if (row == n) {
            res++;
            return;
        }
        
        std::vector<int> unassigned_copy = unassigned_cols;
        for (int col : unassigned_copy) {
            int curr_neg_diag = row - col + n;
            int curr_pos_diag = row + col;
            
            if (neg_diagonal[curr_neg_diag] || pos_diagonal[curr_pos_diag]) 
                continue;

            cols[col]++;
            neg_diagonal[curr_neg_diag]++;
            pos_diagonal[curr_pos_diag]++;
            unassigned_cols.erase(std::find(unassigned_cols.begin(), unassigned_cols.end(), col));

            backtrack(row + 1);
            
            cols[col]--;
            neg_diagonal[curr_neg_diag]--;
            pos_diagonal[curr_pos_diag]--;
            unassigned_cols.push_back(col);
        }
    }
};

int main () {
    std::cout << "Hello World\n";

    Solution sol = Solution();
    
    std::vector<std::tuple<int, int>> tests =  {
        {1, 1},
        {2, 0},
        {3, 0},
        {4, 2}, 
        {5, 10},
        {6, 4},
        {7, 40},
        {8, 92},
        {9, 352},
        {15, 2279184},
    };
    
    std::vector<bool> all_tests;
    std::vector<std::tuple<int, int>> res;
    std::vector<std::tuple<int, int, int>> failed;
    bool ok = true;
    
    auto start = std::chrono::high_resolution_clock::now();
    int i = 1;
    for (const auto& test : tests) {
        int n, expected;
        std::tie(n, expected) = test;
        int output = sol.totalNQueens(n);
        res.push_back({output, expected});
        if (output != expected) {
            ok = false;
            failed.push_back({i, output, expected});
            all_tests.push_back(false);
            i++;
            continue;
        }
        all_tests.push_back(true);
        i++;
    }

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "This run took " << duration.count() << " microseconds." << std::endl;
    
    if (ok) {
        std::cout << std::endl;
        std::cout << "\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/ Passed All Tests \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/" << std::endl;
        std::cout << std::endl;
    }
    else {
        std::cout << "---------------------------------- Failed Tests ----------------------------------" << std::endl;
        for (const auto& fail : failed) {
            int test_num, output, expected;
            std::tie(test_num, output, expected) = fail;
            std::cout << "Test Number: " << test_num << std::endl;
            std::cout << "    Output:   " << output << std::endl;
            std::cout << "    Expected: " << expected << std::endl;
        }
        std::cout << std::endl;
        std::cout << "----------------------------------- All Tests ------------------------------------" << std::endl;
        i = 0;
        for (const auto& r : res) {
            int o, e;
            std::tie(o, e) = r;
            std::cout << "Test Number: " << i + 1;
            if (all_tests[i]) std::cout << " Pass" << std::endl;
            else std::cout << " Failed" << std::endl;
            std::cout << "    Output:   " << o << std::endl;
            std::cout << "    Expected: " << e << std::endl;
            std::cout << std::endl;
            i++;
        }
    }
}
