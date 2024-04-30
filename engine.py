
class chessEngine:
    def __init__(self, FENString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        
        self.board = [[None for i in range(8)] for j in range(8)]
        self.turn = 0
        self.castle = {"K": True, "Q": True, "k": True, "q": True}
        self.enpassant = None

    

    def FENParser(self, FENString):
        
