
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
        RookDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        BishopDirections = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        KnightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        PawnMoves = [(1, 1), (1, -1)]

        for move in RookDirections:
            i, j = kingpos
            while 0 <= i + move[0] < 8 and 0 <= j + move[1] < 8:
                i += move[0]
                j += move[1]
                if self.board[i][j] is not None:
                    if self.board[i][j] == "R" or self.board[i][j] == "Q":
                        return True
                    else:
                        break

        for move in BishopDirections:
            i, j = kingpos
            while 0 <= i + move[0] < 8 and 0 <= j + move[1] < 8:
                i += move[0]
                j += move[1]
                if self.board[i][j] is not None:
                    if self.board[i][j] == "B" or self.board[i][j] == "Q":
                        return True
                    else:
                        break

        for move in KnightMoves:
            i += move[0]
            j += move[1]
            if  0 <= i + move[0] < 8 and 0 <= j + move[1] < 8:
                if self.board[i][j] is not None:
                    if self.board[i][j] == "N":
                        return True
                    
        for move in PawnMoves:
            i += move[0]
            j += move[1]
            if  0 <= i + move[0] < 8 and 0 <= j + move[1] < 8:
                if self.board[i][j] is not None:
                    if self.board[i][j] == "P":
                        return True
                    

        return False
    
    def isCheckmate(self, color):
        pass


    def CheckMove(self, move):
        pass



            




                


    

        
