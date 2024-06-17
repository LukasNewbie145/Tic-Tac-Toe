import pygame
import sys
from Board import Board
from game import Game


def main():
    pygame.init()

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = Board(screen)
    game = Game(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouse_x, mouse_y = event.pos
                clicked_row = mouse_y // 100
                clicked_col = mouse_x // 100
                game.handle_click(clicked_row, clicked_col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.restart_game()

        board.draw_board()
        board.draw_marks(game.board_state)

        if game.game_over:
            board.display_game_over_message(game.winner)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()