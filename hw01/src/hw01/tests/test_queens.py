import unittest
from src.eight_queens import EightQueens

class TestEightQueens(unittest.TestCase):
    def test_4_queens(self):
        solver = EightQueens(4)
        sols = solver.solve()
        self.assertEqual(len(sols), 2)

if __name__ == '__main__':
    unittest.main()
