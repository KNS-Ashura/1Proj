from random import randint

class Game:
    def __init__(self):
        #plateau principale
        self.__board = [[],[],[],[]]
        
        #quatres sections du plateau recto
        self.__square_1 = []
        self.__square_2 = []
        self.__square_3 = []
        self.__square_4 = []
        
        self.__square_list = [self.__square_1, self.__square_2, self.__square_3, self.__square_4]
        
    def create_square(self,square):
        square = [[],[],[],[]]
        for i in range(len(square)):
            square[i] = [randint(1,4),randint(1,4),randint(1,4),randint(1,4)]
        
        return square
                
    def create_board(self):
        self.__board[0] = self.create_square(self.__square_1)
        self.__board[1] = self.create_square(self.__square_2)
        self.__board[2] = self.create_square(self.__square_3)
        self.__board[3] = self.create_square(self.__square_4)
        
        return self.__board
    
    def return_square(self,square):
        new_square = []
        for i in range(len(square)):
            for j in range(len(square)):
                pass
                

    
    def get_square(self,x):
        return self.__square_list[x]
 
    def get_board(self):
        return self.__board
        
    def tower_possible_move(self, x_start, y_start, x_end, y_end):
        if x_start != x_end and y_start != y_end:
            return False

        if x_start == x_end:
            step = 1 if y_end > y_start else -1
            for y in range(y_start + step, y_end, step):
                if self.get_board()[x_start][y] != 0:
                    return False

        elif y_start == y_end:
            step = 1 if x_end > x_start else -1
            for x in range(x_start + step, x_end, step):
                if self.get_board()[x][y_start] != 0:
                    return False

        if self.get_board()[x_end][y_end] != 0:
            return False

        return True
    
    def possible_move_king(self,start_y,start_x): #comme la reine mais max une case
        pass
    
    def possible_move_bishop(self):
        pass
    
obj = Game()

print(obj.create_board())
print(obj.return_square(obj.get_square(0)))
print(obj.get_square(0))
