import time

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        max_size = len(words)

        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word

        def backTracking(i: int, j: int, parent: dict) -> None:
            char = board[i][j]
            if char == '#' or char not in parent: return

            child = parent[char]
            match_found = child.pop('$', False)
            if match_found:
                res.append(match_found)
            if len(res) == max_size: return

            board[i][j] = '#'
            if i > 0:     backTracking(i - 1, j, child)
            if j > 0:     backTracking(i, j - 1, child)
            if i < m - 1: backTracking(i + 1, j, child)
            if j < n - 1: backTracking(i, j + 1, child)
            board[i][j] = char

            if not child:
                parent.pop(char)
        
        res = []
        i, j = 0, 0
        while i < m:
            while j < n:
                if board[i][j] in root:
                    backTracking(i, j, root)
                    if len(res) == max_size:
                        return res
                j += 1
            i += 1
            j = 0
        return res

if __name__ == "__main__":
    sol = Solution()
    tests =  [
                ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"], ["eat","oath"]),
                ([["a","b"],["c","d"]], ["abcb"], []),
                ([["o","a","b","n"], ["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"], ["oa","oaa"]),
                ([["a","a"]], ["aaa"], set()),
                ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","hklf", "hf"], ["oath","eat","hklf","hf"]),
                ([["a","b","c"],["a","e","d"],["a","f","g"]], ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"], ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]),
                ([["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"], ["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]], ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], ['aaaaaa', 'aaa', 'aaaaa', 'aaaaaaaa', 'aaaa', 'aaaaaaaaaa', 'a', 'aa', 'aaaaaaaaa', 'aaaaaaa']),
                ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"], ["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"])
            ]
    
    all_tests = []
    res = []
    failed = []
    ok = True
    
    start_time = time.time()
    for i, test in enumerate(tests, start=1):
        board, words, expected = test
        output = sol.findWords(board, words)
        res.append((output, expected))
        if not all(x in output for x in expected):
            ok = False
            failed.append((i, sorted(output), sorted(expected)))
            all_tests.append(False)
            continue
        all_tests.append(True)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Runtime: {round(elapsed_time, 9)}s")
    
    if ok:
        print()
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ Passed All Tests \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print()
    else:
        print("---------------------------------- Failed Tests ----------------------------------")
        for fail in failed:
            test_num, output, expected = fail
            print(f"Test Number: {test_num}") 
            print(f"    Output:   {output}")
            print(f"    Expected: {expected}")
        print()
        print("----------------------------------- All Tests ------------------------------------")
        for i, (o, e) in enumerate(res):
                print(f"Test Number: {i+1}    ", end="") 
                print("Pass") if all_tests[i] else print("Failed")
                print(f"    Output:   {o}")
                print(f"    Expected: {e}")
                print()
                