import random

def generate_board(words, spangram, m, n):
    board = [['' for _ in range(n)] for _ in range(m)]

    # Place the spangram on the board
    spangram_start_col = random.randint(0, n - len(spangram))
    for i, char in enumerate(spangram):
        board[0][spangram_start_col + i] = char

    # Place the other words on the board
    word_index = 0
    for row in range(1, m):
        col = 0
        while col < n and word_index < len(words):
            word = words[word_index]
            if col + len(word) <= n:
                for i, char in enumerate(word):
                    board[row][col + i] = char
                col += len(word) + 1  # Add a space between words
                word_index += 1
            else:
                break

    return board

def print_board(board):
    for row in board:
        print(' '.join(char if char else '.' for char in row))

if __name__ == "__main__":
    theme = "Panoramic Views"
    spangram = "Scenic Overlooks"
    words = ["Vista", "Frame", "Sash", "Pane", "Gaze", "Focal"]

    m = 6
    n = 7

    board = generate_board(words, spangram, m, n)
    print(f"Theme: {theme}")
    print(f"Spangram: {spangram}")
    print("Board:")
    print_board(board)
