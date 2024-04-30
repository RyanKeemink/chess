
class chessEngine:
    def __init__(self, FENString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        
        self.board = [[None for i in range(8)] for j in range(8)]
        self.turn = 0
        self.castle = {"K": True, "Q": True, "k": True, "q": True}
        self.enpassant = None

    

    def FENParser(self, FENString):
        FEN = FENString.split(" ")
        board = FEN[0].split("/")
        for i in range(8):
            j = 0
            for c in board[i]:
                if c.isnumeric():
                    j += int(c)
                else:
                    self.board[i][j] = c
                    j += 1
        self.turn = FEN[1]
        self.castle = FEN[2]
        self.enpassant = FEN[3]
        self.halfmove = FEN[4]
        self.fullmove = FEN[5]

    

        
