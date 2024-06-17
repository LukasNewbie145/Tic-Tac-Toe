import pygame


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

    def draw_board(self):
        self.screen.fill(self.white)
        for row in range(1, 3):
            pygame.draw.line(self.screen, self.black, (0, row * 100), (self.screen_width, row * 100), 2)
            pygame.draw.line(self.screen, self.black, (row * 100, 0), (row * 100, self.screen_height), 2)

    def draw_marks(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    color = self.red
                elif board[row][col] == 'O':
                    color = self.blue
                else:
                    continue
                text = self.font.render(board[row][col], True, color)
                self.screen.blit(text, (col * 100 + 30, row * 100 + 15))

    def display_game_over_message(self, winner):
        if winner:
            message = f'{winner} wins! Press R to Restart'
        else:
            message = 'It\'s a Draw! Press R to Restart'
        text = self.small_font.render(message, True, self.black)
        self.screen.blit(text, (15, 130))
