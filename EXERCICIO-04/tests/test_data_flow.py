import unittest
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To12X3
from src.invalid_position_exception import InvalidPositionException
from src.puzzle_game import PuzzleGame

class DataFlowTests(unittest.TestCase):

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        # 1  2
        # -  3
        shuffler.shuffle(self.puzzle_game)

    # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-3-5
    # Acha uma posição vazia
    # def test_case_1_2_3_5(self):
    #     print("test_case_1_2_3_5")
    #     # IMPLICIT FIXTURE SETUP
    #     # INLINE FIXTURE SETUP
    #     line = 2
    #     column = 1
    #     excpected_result = ' ' #tile in line 2, column 1 is empty, should return empty
    #     # EXERCISE SUT
    #     result = self.puzzle_game.get_tile(line, column)
    #     # RESULT VERIFICATION: 
    #     self.assertEqual(result, excpected_result)

    # # TEST CASE FOR ALL C-USES OF LINE AND COLUMN: 1-2-3-4
    # # AND
    # # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-3-4
    # # Retorna a peça
    # def test_case_1_2_3_4(self):
    #     print("test_case_1_2_3_4")
    #     # IMPLICIT FIXTURE SETUP
    #     # INLINE FIXTURE SETUP
    #     line = 1
    #     column = 2
    #     excpected_result = 2 #tile in line 1, column 2 is 2
    #     # EXERCISE SUT
    #     result = self.puzzle_game.get_tile(line, column)
    #     # RESULT VERIFICATION
    #     self.assertEqual(result, excpected_result)

    # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-6
    # Erro
    def test_case_1_2_6(self):
        print("test_case_1_2_6")
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 3
        # RESULT VERIFICATION
        with self.assertRaises(InvalidPositionException):
            # EXERCISE SUT
            self.puzzle_game.get_tile(line, column)


if __name__ == '__main__':
    unittest.main()