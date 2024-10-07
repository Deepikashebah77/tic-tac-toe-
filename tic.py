import pygame as pg
import sys
import time

# Initialize Pygame
pg.init()

# Define constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
X_COLOR = (0, 0, 255)
O_COLOR = (255, 0, 0)
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Create the game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Tic Tac Toe')

# Define fonts
font = pg.font.Font(None, 74)

# Initialize game variables
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
current_player = 'X'
winner = None
game_over = False

def draw_lines():
    """Draw the grid lines on the board."""
    pg.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_marks():
    """Draw X and O marks on the board."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pg.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + 15, row * SQUARE_SIZE + 15), 
                             ((col + 1) * SQUARE_SIZE - 15, (row + 1) * SQUARE_SIZE - 15), LINE_WIDTH)
                pg.draw.line(screen, X_COLOR, ((col + 1) * SQUARE_SIZE - 15, row * SQUARE_SIZE + 15), 
                             (col * SQUARE_SIZE + 15, (row + 1) * SQUARE_SIZE - 15), LINE_WIDTH)
            elif board[row][col] == 'O':
                pg.draw.circle(screen, O_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                               SQUARE_SIZE // 3, LINE_WIDTH)

def check_winner():
    global winner
    # Check rows and columns
    for i in range(BOARD_ROWS):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            winner = board[i][0]
            pg.draw.line(screen, (0, 255, 0), (0, i * SQUARE_SIZE + SQUARE_SIZE // 2), 
                         (WIDTH, i * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
            return
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            winner = board[0][i]
            pg.draw.line(screen, (0, 255, 0), (i * SQUARE_SIZE + SQUARE_SIZE // 2, 0), 
                         (i * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT), LINE_WIDTH)
            return

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pg.draw.line(screen, (0, 255, 0), (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pg.draw.line(screen, (0, 255, 0), (WIDTH - 15, 15), (15, HEIGHT - 15), LINE_WIDTH)
        return

    # Check for draw
    if all(cell is not None for row in board for cell in row):
        winner = 'Draw'

def draw_status():
    """Draw the status message on the board."""
    if winner:
        if winner == 'Draw':
            message = 'Draw!'
        else:
            message = f'{winner} Wins!'
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def reset_game():
    """Reset the game to start a new round."""
    global board, current_player, winner, game_over
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    current_player = 'X'
    winner = None
    game_over = False
    screen.fill(WHITE)
    draw_lines()

def handle_click(pos):
    """Handle mouse click events."""
    global current_player, winner, game_over
    if winner or game_over:
        reset_game()
        return
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    if board[row][col] is None:
        board[row][col] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        check_winner()
        draw_marks()
        draw_status()


def main():
    screen.fill(WHITE)
    draw_lines()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                handle_click(event.pos)
        pg.display.update()

if __name__ == "__main__":
    main()
