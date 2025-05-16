import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def solveSudoku(self, board):
        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])
        def place_number(d, row, col):
            board[row][col] = d
            rows[row].add(d)
            cols[col].add(d)
            boxes[box_index(row, col)].add(d)
        def remove_number(d, row, col):
            board[row][col] = '.'
            rows[row].remove(d)
            cols[col].remove(d)
            boxes[box_index(row, col)].remove(d)
        def place_next_numbers(row, col):
            if col == 8 and row == 8:
                nonlocal solved
                solved = True
            elif col == 8:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)
        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in '123456789':
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        box_index = lambda row, col: (row // 3) * 3 + col // 3
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = board[i][j]
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[box_index(i, j)].add(d)
        solved = False
        backtrack()
        return board

    def test_solveSudoku(self):
        test_cases = [
            ([['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']],
             [['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]),
            ([['.','.','9','7','4','8','.','.','.'],['7','.','.','.','.','.','.','.','.'],['.','2','.','1','.','9','.','.','.'],['.','.','7','.','.','.','2','4','.'],['.','6','4','.','1','.','5','9','.'],['.','9','8','.','.','.','3','.','.'],['.','.','.','8','.','3','.','2','.'],['.','.','.','.','.','.','.','.','6'],['.','.','.','2','7','5','9','.','.']],
             [['5','1','9','7','4','8','6','3','2'],['7','8','3','6','5','2','4','1','9'],['4','2','6','1','3','9','8','7','5'],['3','5','7','9','8','6','2','4','1'],['2','6','4','3','1','7','5','9','8'],['1','9','8','5','2','4','3','6','7'],['9','7','5','8','6','3','1','2','4'],['8','3','2','4','9','1','7','5','6'],['6','4','1','2','7','5','9','8','3']]),
        ]
        passed = 0
        for idx, (board, expected) in enumerate(test_cases, 1):
            import copy
            result = self.solveSudoku(copy.deepcopy(board))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={board}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_solveSudoku()

if __name__ == "__main__":
    run_tests()
