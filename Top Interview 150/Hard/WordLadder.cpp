#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <chrono>
#include <tuple>
#include <queue>

class Solution {
    public:
    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) 
            return 0;
        if (beginWord == endWord)
            return 1;
        int length = endWord.size();
        
        std::unordered_map<int, std::unordered_set<char> > char_map;
        for (const std::string& word : wordSet) {
            for (int i = 0; i < length; i++) {
                char_map[i].insert(word[i]);
            }
        }
        std::queue<std::string> forward_q;
        forward_q.push(beginWord);
        std::queue<std::string> backward_q;
        backward_q.push(endWord);
        std::unordered_set<std::string> forward_visited;
        forward_visited.insert(beginWord);
        std::unordered_set<std::string> backward_visited;
        backward_visited.insert(endWord);
        
        int steps = 1;
        while (!forward_q.empty() && !backward_q.empty()) {
            if (forward_q.size() > backward_q.size()) {
                swap(forward_q, backward_q);
                swap(forward_visited, backward_visited);
            }
            int size = forward_q.size();
            while (size > 0) {
                std::string curr = forward_q.front();
                forward_q.pop();
                for (int i = 0; i < length; ++i) {
                    for (const char& ch : char_map[i]) {
                        if (ch != curr[i]) {
                            std::string neighbor = curr.substr(0, i) + ch + curr.substr(i + 1);
                            if (wordSet.count(neighbor) && !forward_visited.count(neighbor)) {
                                if (backward_visited.count(neighbor))
                                    return steps + 1;
                                forward_visited.insert(neighbor);
                                forward_q.push(neighbor);
                            }
                        }
                    }
                }
                size--;
            }
            steps++;
        }
        return 0;
    }
};

int main() {
    Solution sol = Solution();
    std::vector<std::tuple<std::string, std::string, std::vector<std::string>, int>> tests =  {
        {"hit", "cog", {"hot","dot","dog","lot","log","cog"}, 5},
        {"hit", "cog", {"hot","dot","dog","lot","log"}, 0},
        {"hot", "dog", {"hot","dog"}, 0},
        {"hit", "cog", {"hot","dot","tog","cog"}, 0},
        {"ymain", "oecij", {"ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"}, 10},
    };
    
    std::vector<std::tuple<int, int>> res;
    std::vector<std::tuple<int, int, int>> failed;
    bool ok = true;
    
    auto start = std::chrono::high_resolution_clock::now();
    int i = 0;
    for (const auto& test : tests) {
        std::string beginWord, endWord;
        std::vector<std::string> wordList;
        int expected;
        std::tie(beginWord, endWord, wordList, expected) = test;

        int output = sol.ladderLength(beginWord, endWord, wordList);
        res.push_back({output, expected});
        if (output != expected) {
            ok = false;
            failed.push_back({i, output, expected});
        }
        i++;
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "This run took " << duration.count() << " microseconds." << std::endl;
    
    if (ok)
        std::cout << "Passed All Tests\n";
    else{
        std::cout << "Failed Tests:\n";
        for (const auto& fail : failed) {
            int test_num, output, expected;
            std::tie(test_num, output, expected) = fail;
            std::cout << "Test Number: " << test_num << ", Output: " << output << ", Expected: " << expected << std::endl;
        }
        std::cout << std::endl;
    }
    for (const auto& result : res) {
        int x, y;
        std::tie(x, y) = result;
        std::cout << "(" << x << ", " << y << ")\n"; 
    }
    return 0;
}