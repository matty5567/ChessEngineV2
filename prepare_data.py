
import zipfile
import numpy


class game_data():
  def __init__(self, num_games, train_test_split):
    self.num_games        = num_games
    self.train_test_split = train_test_split

    self.train_data_states = []
    self.test_data_states  = []
    self.train_data_labels = []
    self.test_data_labels  = []

    self.setup()

  
  def _board_to_tensor(self, board):
    '''
    Represents the board as (8, 8, 5) tensor. First 3 dims are 3 bit reprentation
    of pieces. 4th dimension represents the colour of the respective piece. 5th
    dimension is which player has next move
    '''

    torch_board = np.zeros((8, 8, 5))
    for x in range(8):
      for y in range(8):
        piece = board.piece_at(x + y*8)
        if piece == None:
          torch_board[y, x, 0] = 0
          torch_board[y, x, 1] = 0
        else:
          piece_type = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                        "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[piece.symbol()]
          
          peice = f'{piece_type:04b}'

          # print(piece_type, ':', peice)

          color = piece.color
          torch_board[y, x, 0] = int(peice[0])
          torch_board[y, x, 1] = int(peice[1])
          torch_board[y, x, 2] = int(peice[2])
          torch_board[y, x, 3] = int(peice[3])


    # White to move represented with 1
    torch_board[:, :, 4] = {True:1, False:-1}[board.turn]

    return torch_board


  def setup(self):
    

    self.pgn = open('/content/data/AepliBase.pgn')
    print('found pgn file')

    counter = 0
    num_states = 0
    num_white_wins = 0
    while True:

      if counter > self.num_games:
        break
      
      try:
        game = chess.pgn.read_game(self.pgn)

        match_result = game.headers['Result']

        if match_result == '*':
          continue

        result = {'1-0':1, '1/2-1/2':0,'0-1':-1}[match_result]

        if result == 1:
          num_white_wins += 1

        board = game.board()
        for move in game.main_line():
          board.push(move)
          board_tensor = self._board_to_tensor(board)

          if counter < self.num_games * self.train_test_split:
            self.train_data_states.append(board_tensor)
            self.train_data_labels.append(result)

          else:
            self.test_data_states.append(board_tensor)
            self.test_data_labels.append(result)
          
          num_states += 1
      
        counter += 1
        if counter % 1000 == 0:
          print(f'{counter} / {self.num_games}, total number of states: {num_states}')
      except Exception as e:
        print(e)
        break


data = game_data(30000, 0.8)


np.savez('/content/drive/MyDrive/train_data.npz', np.array(data.train_data_states), np.array(data.train_data_labels))
np.savez('/content/drive/MyDrive/test_data.npz', np.array(data.test_data_states), np.array(data.test_data_labels))