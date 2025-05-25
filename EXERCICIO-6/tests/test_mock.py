import unittest
from unittest.mock import patch
from src.puzzle_game import PuzzleGame 
from src.puzzle_game_with_mock import PuzzleGameWithPlayer
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To12X3

class MockTests(unittest.TestCase):

    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
        self.puzzle_game_with_player = PuzzleGameWithPlayer(2, "Victor do Valle")
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(self.puzzle_game)
        shuffler.shuffle(self.puzzle_game_with_player)

        # Posição inincial do tabuleiro (depois do embaralhamento):
        # 1  2
        # -  3
        
        

    '''
    PARTE 1 
    ITEM 1: Faça dois testes sem mock para o método get_tile da classe PuzzleGame.
    '''
    # Teste 1
    def test_get_tiles_1_2_e_2_2_in_board_of_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("RIGHT")
        # RESULT VERIFICATION: 
        self.assertEqual(1,   self.puzzle_game.get_tile(1, 1))
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))
        self.assertEqual(3,   self.puzzle_game.get_tile(2, 1))
        self.assertEqual(' ',   self.puzzle_game.get_tile(2, 2))

        # 1  2
        # 3  -

    # Teste 2
    def test_get_tiles_1_1_e_2_1_in_board_of_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 1)
        # RESULT VERIFICATION: 
        self.assertEqual(' ',   self.puzzle_game.get_tile(1, 1))
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))
        self.assertEqual(1,   self.puzzle_game.get_tile(2, 1))
        self.assertEqual(3,   self.puzzle_game.get_tile(2, 2))

        # - 2
        # 1 3

    '''
    PARTE 1 
    ITEM 2: Faça os mesmos dois testes com mocks para o método get_tile da classe PuzzleGame.
    '''
    # Teste 1 com Mock
    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_get_tiles_1_2_e_2_2_in_board_of_2x2_with_mock(self, mock_board_get_tile):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("RIGHT")
        # RESULT VERIFICATION: 
        mock_board_get_tile.return_value = 1
        self.assertEqual(1, self.puzzle_game.get_tile(1, 1))
        
        mock_board_get_tile.return_value = 2
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))

        mock_board_get_tile.return_value = 3
        self.assertEqual(3, self.puzzle_game.get_tile(2, 1))

        mock_board_get_tile.return_value = ' '
        self.assertEqual(' ', self.puzzle_game.get_tile(2, 2))

    # Teste 2 com Mock
    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_get_tiles_1_1_e_2_1_in_board_of_2x2_with_mock(self, mock_board_get_tile):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 1)
        # RESULT VERIFICATION: 
        mock_board_get_tile.return_value = ' '
        self.assertEqual(' ', self.puzzle_game.get_tile(1, 1))
        
        mock_board_get_tile.return_value = 2
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))

        mock_board_get_tile.return_value = 1
        self.assertEqual(1, self.puzzle_game.get_tile(2, 1))

        mock_board_get_tile.return_value = 3
        self.assertEqual(3, self.puzzle_game.get_tile(2, 2))

    '''
    PARTE 2
    ITEM 1: Faça dois testes sem mock envolvendo o método end_of_the_game da classe PuzzleGameWithPlayer.
    '''
    # Teste 1
    def test_end_of_the_game_true_in_board_of_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game_with_player.move_empty_tile("RIGHT")
        finished = self.puzzle_game_with_player.end_of_the_game()
        # RESULT VERIFICATION: 
        self.assertEqual('Saved', finished)

        # 1  2
        # 3  -

    # # Teste 2
    def test_end_of_the_game_false_in_board_of_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game_with_player.move_empty_tile("UP")
        finished = self.puzzle_game_with_player.end_of_the_game()
        # RESULT VERIFICATION: 
        self.assertEqual('Game not finished', finished)

    '''
    PARTE 2
    ITEM 2: Faça os mesmos dois testes envolvendo o método end_of_the_game da classe PuzzleGameWithPlayer utilizando mock para o método save_game_to_file.
    '''
    # Teste 1 com mock
    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_true_in_board_of_2x2_with_mock(self, mock_save_game_to_file):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game_with_player.move_empty_tile("RIGHT")
        # RESULT VERIFICATION: 
        mock_save_game_to_file.return_value = 'Saved'
        self.assertEqual('Saved', self.puzzle_game_with_player.end_of_the_game())


    # # Teste 2 com mock
    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_false_in_board_of_2x2_with_mock(self, mock_save_game_to_file):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        mock_save_game_to_file.return_value = 'Saved'
        finished = self.puzzle_game_with_player.end_of_the_game()
        # RESULT VERIFICATION: 
        self.assertEqual('Game not finished', finished)
