import unittest
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32
from src.puzzle_game import PuzzleGame


class TestStatmentCoverage(unittest.TestCase):

    # # 1 - 2(T) - 3(T) -  4(T) - 5(T) - 6(T) - 7(T) - 8(T)
    def test_pega_valor_com_linha_com_valor_coluna_vazia(self):
         # INLINE FIXTURE SETUP
         puzzle_game = PuzzleGame(2)
         shuffler = TestingShufflerPuzzleGame2x2To1X32()
         shuffler.shuffle(puzzle_game)
         # EXERCISE SUT
         result = puzzle_game.get_tile(2, 1)
         # RESULT VERIFICAtION
         self.assertEqual(3, result)
    
    # 1 - 2(T) - 3(T) -  4(T) - 5(T) - 6(F) - 9
    def test_pega_valor_vazio(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # EXERCISE SUT
        result = puzzle_game.get_tile(1, 2)
        # RESULT VERIFICAtION
        self.assertEqual(' ', result)

    # 1 - 2(F) - 10
    def test_linha_menor_que_zero(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # # EXERCISE SUT
        with self.assertRaises(InvalidPositionException):
            puzzle_game.get_tile(-1, 2)
        
    # 1 - 2(T) - 3(F) - 10
    def test_linha_maior_que_numbero_linhas(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # # EXERCISE SUT
        with self.assertRaises(InvalidPositionException):
            puzzle_game.get_tile(3, 2)
    
   # 1 - 2(T) - 3(T) - 4(F) - 10
    def test_coluna_menor_que_zero(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # # EXERCISE SUT
        with self.assertRaises(InvalidPositionException):
            puzzle_game.get_tile(1, -1)
        

    # 1 - 2(T) - 3(T) - 4(T) - 5(F) - 10    
    def test_coluna_maior_que_numbero_linhas(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # # EXERCISE SUT
        with self.assertRaises(InvalidPositionException):
            puzzle_game.get_tile(1, 3)
    
    
    # 1 - 2(T) - 3(T) -  4(T) - 5(T) - 6(T) - 7(F) - 9
    def test_pega_valor_com_linha_vazia_coluna_com_valor(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        # EXERCISE SUT
        result = puzzle_game.get_tile(1, 1)
        # RESULT VERIFICAtION
        self.assertEqual(1, result)
        


if __name__ == '__main__':
    unittest.main()