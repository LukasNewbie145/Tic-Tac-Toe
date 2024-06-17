class Game:
    def __init__(self, board):
        self.board = board
        self.board_state = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def handle_click(self, row, col):
        if self.board_state[row][col] == '' and not self.game_over:
            self.board_state[row][col] = self.current_player
            if self.check_winner():
                self.game_over = True
            elif self.check_draw():
                self.game_over = True
                self.winner = None
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.board_state[row][0] == self.board_state[row][1] == self.board_state[row][2] != '':
                self.winner = self.board_state[row][0]
                return True
        for col in range(3):
            if self.board_state[0][col] == self.board_state[1][col] == self.board_state[2][col] != '':
                self.winner = self.board_state[0][col]
                return True
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] != '':
            self.winner = self.board_state[0][0]
            return True
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] != '':
            self.winner = self.board_state[0][2]
            return True
        return False

    def check_draw(self):
        return all(self.board_state[row][col] != '' for row in range(3) for col in range(3))

    def restart_game(self):
        self.board_state = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None