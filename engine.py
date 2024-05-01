
class chessEngine:
    def __init__(self, FENString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        
        self.board = [[None for i in range(8)] for j in range(8)]
        self.turn = 0
        self.castle = {"K": True, "Q": True, "k": True, "q": True}
        self.enpassant = None

    

    def FENParser(self, FENString):
        fen = FENString.split(" ")
        board = fen[0].split("/")
        for i in range(8):
            j = 0
            for c in board[i]:
                if c.isnumeric():
                    j += int(c)
                else:
                    self.board[i][j] = c
                    j += 1
        self.turn = fen[1]
        self.castle = fen[2]
        self.enpassant = fen[3]
        self.halfmove = fen[4]
        self.fullmove = fen[5]

    def isCheck(self, color):
        if color == "w":
            king = "K"
        else:
            king = "k"
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == king:
                    kingpos = (i, j)
                    break
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for d in directions:
            x, y = kingpos
            steps = 0
            while True:
                steps += 1
                x += d[0]
                y += d[1]
                if x < 0 or x > 7 or y < 0 or y > 7:
                    break
                if self.board[x][y] != None:
                    if self.board[x][y].islower() == color.islower():
                        break
                    if self.board[x][y].lower() == "q" or self.board[x][y].lower() == "r":
                        return True
                    break
                


    

        
