import chess

def start_game():
    board = chess.Board()
    return board.fen()

# Quick test so you can run "python chess_engine.py" and see it work
if __name__ == "__main__":
    print("Starting position FEN:")
    print(start_game())
