import time

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row:int) -> None:
            nonlocal res
            if row == n:
                res += 1
                return

            for col in unassigned_cols.copy():
                curr_neg_diag = row - col + n
                curr_pos_diag = row + col
                
                if neg_diagonal[curr_neg_diag] or pos_diagonal[curr_pos_diag]:
                    continue

                cols[col] = True
                neg_diagonal[curr_neg_diag] = True
                pos_diagonal[curr_pos_diag] = True
                unassigned_cols.remove(col)

                backtrack(row + 1)
                
                cols[col] = False
                neg_diagonal[curr_neg_diag] = False
                pos_diagonal[curr_pos_diag] = False
                unassigned_cols.append(col)

        res = 0
        cols, neg_diagonal, pos_diagonal = [False] * n, [False] * (n * 2), [False] * (n * 2)
        unassigned_cols = list(i for i in range(n))
        backtrack(0)
        return res

if __name__ == "__main__":
    sol = Solution()
    tests =  [
                (1, 1),
                (2, 0),
                (3, 0),
                (4, 2), 
                (5, 10),
                (6, 4),
                (7, 40),
                (8, 92),
                (9, 352),
                # (15, 2279184),
            ]
    
    all_tests = []
    res = []
    failed = []
    ok = True
    
    start_time = time.time()
    for i, test in enumerate(tests, start=1):
        n, expected = test
        output = sol.totalNQueens(n)
        res.append((output, expected))
        if output != expected:
            ok = False
            failed.append((i, output, expected))
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