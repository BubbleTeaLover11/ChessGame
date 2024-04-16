#Name: William Chen
#Github Username: BubbleTeaLover11
#Date: 11.21.2023
#Description: Portfolio Project, Create a chess game that wins by taking all types of a given piece

class Piece:
    """
    Chess Piece class
    Pieces in this class will be put in the board and be used
    """

    def __init__(self, color):
        """
        Initialization of Chess Piece
        color = Piece Color
        """
        self._color = color
        self._piece = None


    def get_color(self):
        """
        Gets color of piece
        Returns: Piece Color
        """
        return self._color
    
    def get_piece(self):
        """
        Gets piece color and type
        Returns: String for piece color and piece type
        """
        return str(self._color) + " " + str(self._piece)
    
    def get_piece_type(self):
        """
        Gets piece color and type
        Returns: String for piece type
        """
        return self._piece
    
class Pawn(Piece):
    """
    Pawn Class
    Pawns are given certain movement on certain spaces, no worries about pawn promotion
    """

    def __init__(self, color):
        """
        Initialization of Pawn Piece
        color = Piece color
        """
        self._color = color
        self._piece = 'Pawn'

class Rook(Piece):
    """
    Rook Class
    Rooks are given certain movement and will be used in the ChessVar to check if the movement is legal or illegal
    """
    def __init__(self, color):
        """
        Initialization of Rook Piece
        color = Piece Color
        """
        self._color = color    
        self._piece = 'Rook'

class Knight(Piece):
    """
    Knight Class
    Knights are given certain movement and will be used in the ChessVar to check if the movement is legal or illegal
    """

    def __init__(self, color):
        """
        Initialization of Knight Piece
        color = Piece Color    
        """
        self._color = color   
        self._piece = 'Knight'

class Bishop(Piece):
    """
    Bishop Class
    Knights are given certain movement and will be used in the ChessVar to check if the movement is legal or illegal
    """

    def __init__(self, color):
        """
        Initialization of Bishop Piece
        color = Piece Color
        """
        self._color = color
        self._piece = 'Bishop'

class King(Piece):
    """
    King Class
    Kings are given certain movement and will be used in the ChessVar to check if the movement is legal or illegal
    """

    def __init__(self, color):
        """
        Initialization of King Piece
        color = Piece Color
        """
        self._color = color    
        self._piece = 'King'

class Queen(Piece):
    """
    Queen class
    Queens are given certain movement and will be used in the ChessVar to check if the movement is legal or illegal
    """

    def __init__(self, color):
        """
        Initialization of Queen Piece
        color = Piece Color
        """
        self._color = color
        self._piece = 'Queen'

class IncorrectTurn(Exception):
    """
    Incorrect Turn exception for player for make_move method
    """
    pass

class OutOfBounds(Exception):
    """
    Out of Bounds exception for chess move for make_move method
    """
    pass

class IllegalMove(Exception):
    """
    Illegal Move exception for chess game, will apply to movement onto same colorpiece, and improper movement
    """
    pass

class ChessVar:
    """
    Chess Class
    This is the chess board to be used
    """

    def __init__(self):
        """
        Initialization of Chess board
        """
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        board = dict()
        self._black = []    #List of chess pieces
        self._white = []    #List of White chess pieces
        for i in range(1,len(rows) + 1):
            board[i] = [[''] for x in range(len(rows))] #making each square its own individual cell
        for keys, values in board.items():
            if keys == 1:
                color = 'white'
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7] = Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color), Rook(color)
                for i in values:
                    self._white.append(i.get_piece())
            if keys == 2:
                color = 'white'
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7] = Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color)
                for i in values:
                    self._white.append(i.get_piece())
            if keys == 8:
                color = 'black'
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7] = Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color), Rook(color)
                for i in values:
                    self._black.append(i.get_piece())            
            if keys == 7:
                color = 'black'
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7] = Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color), Pawn(color)
                for i in values:
                    self._black.append(i.get_piece())  
        self._state = 'UNFINISHED'
        self._board = board
        self._turn = 'white'

    def show_board(self):
        """
        Shows board of all pieces via print statement
        """
        nums = [1,2,3,4,5,6,7,8]
        for i in nums[::-1]:
            print(i, end = " ")
            print("[", end = " ")
            for j in self._board[i]:
                if type(j) != list:
                    print(j.get_piece(), end = ",")
                else:
                    print(j, end = ",")
            print("]")
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print('/', end = '   ')
        for i in rows:
            print(i, end = '     ')

    def change_turn(self):
        """
        Changes turn of game state
        """
        if self._turn == 'white':
            self._turn = 'black'
            return
        if self._turn == 'black':
            self._turn = 'white'
            return
    
    def get_game_state(self):
        """
        Gets state of the game
        """
        return self._state
    
    def rook_move(self, start, end):
        """
        Rook Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken
        """
        #Rooks can move vertically and horizontally
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        temp_column, temp_row = start_column, start_row
        #Check for that movement is not landing on the same color

        if type(self._board[end_row][end_column]) != list:
            if self._board[temp_row][temp_column].get_color() == self._board[end_row][end_column].get_color():
                raise IllegalMove
        
        #Make sure that it's not moving diagnoally
        if (start_column != end_column) and (start_row != end_row):
            raise IllegalMove
        
        #Check Rook movement for legal move, vert and horz
        #Represents horizontal    
        if start_row == end_row:
            single_horz = int((end_column - start_column) / abs(end_column - start_column))
            while temp_column != end_column:
                temp_column += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_column != end_column):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
            
        #Represents vertical            
        if start_column == end_column: 
            single_horz = int((end_row - start_row) / abs(start_row - end_row))
            while temp_row != end_row:
                temp_row += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_row != end_row):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
    
    def knight_move(self, start, end):
        """
        Knight Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken
        """
        #Knights move in an L pattern (1 left and 2 up, 1 up and 2 left, etc)
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        temp_column, temp_row = start_column, start_row

        #Check for legal movements
        #Can't land on same color
        if type(self._board[end_row][end_column]) != list:
            if self._board[temp_row][temp_column].get_color() == self._board[end_row][end_column].get_color():
                raise IllegalMove
        
        #If not moving in an L shape
        vert_check = abs(start_row - end_row)
        horz_check = abs(end_column - start_column)
        total_mov = horz_check + vert_check
        if total_mov != 3:
            raise IllegalMove
        
        #Represents movement, can skip over pieces
        if type(self._board[end_row][end_column]) != list:
            captured = self._board[end_row][end_column] #Captured
            temp = self._board[start_row][start_column] #Beginning
            self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
            return captured #Piece captured
        
        if type(self._board[end_row][end_column]) == list:
            temp = self._board[start_row][start_column] #Beginning
            self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
            return None #none captured        
    
    def bishop_move(self, start, end):
        """
        Knight Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken
        """
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        temp_column, temp_row = start_column, start_row

        if type(self._board[end_row][end_column]) != list:
            if self._board[temp_row][temp_column].get_color() == self._board[end_row][end_column].get_color():
                raise IllegalMove
            
        vert_check = abs(start_row - end_row)
        horz_check = abs(end_column - start_column)

        if vert_check != horz_check: #Not moving diagonally
            raise IllegalMove
        
        single_vert = int((end_row - start_row) / abs(start_row - end_row)) #Should return either 1 or +1
        single_horz = int((end_column - start_column) / abs(start_column - end_column))

        while temp_column != end_column and temp_row != end_row:
            temp_column += single_horz
            temp_row += single_vert

            space = self._board[temp_row][temp_column]
            #Not on last iteration 
            if type(space) != list and (temp_row != end_row) and (temp_column != end_column):
                raise IllegalMove
            #on last iteration and not moving, captured piece

        if type(self._board[end_row][end_column]) != list:
            captured = self._board[end_row][end_column] #Captured
            temp = self._board[start_row][start_column] #Beginning
            self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
            return captured #Piece captured
        
        if type(self._board[end_row][end_column]) == list:
            temp = self._board[start_row][start_column] #Beginning
            self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
            return None #none captured

    def king_move(self, start, end):
        """
        King Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken
        """
        #Kings can move anywhere within one space
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        temp_column, temp_row = start_column, start_row

        #Check for that movement is not landing on the same color
        if type(self._board[end_row][end_column]) != list:
            if self._board[temp_row][temp_column].get_color() == self._board[end_row][end_column].get_color():
                raise IllegalMove
            
        #Check if it is moving more than 1 space
        vert = abs(start_row - end_row)
        horz = abs(start_column - end_column)

        if vert > 1:
            raise IllegalMove
        if horz > 1:
            raise IllegalMove
        
        #Check King movement for legal moves, diagnoal and straight up to length of the board
        #Represents horizontal    
        if start_row == end_row:
            single_horz = int((end_column - start_column) / abs(end_column - start_column))

            while temp_column!= end_column:
                temp_column += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_column != end_column):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
            
        #Represents vertical            
        if start_column == end_column: 
            single_horz = int((end_row - start_row) / abs(start_row - end_row))

            while temp_row != end_row:
                temp_row += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_row != end_row):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
            
        #Check diagonal movement    
        if (start_column != end_column) and (start_row != end_row):
            single_vert = int((end_row - start_row) / abs(start_row - end_row)) #Should return either 1 or +1
            single_horz = int((end_column - start_column) / abs(start_column - end_column))

            while temp_column != end_column and temp_row != end_row:
                temp_column += single_horz
                temp_row += single_vert
                #Check
                space = self._board[temp_row][temp_column]
                #Not on last iteration 

                if type(space) != list and (temp_row != end_row) and (temp_column != end_column):
                    raise IllegalMove
                #on last iteration and not moving, captured piece

            if type(self._board[end_row][end_column]) != list:
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured

    def queen_move(self, start, end):
        """
        Queen Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken       
        """
        #Queens can move anywhere
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        temp_column, temp_row = start_column, start_row
        #Check for that movement is not landing on the same color

        if type(self._board[end_row][end_column]) != list:
            if self._board[temp_row][temp_column].get_color() == self._board[end_row][end_column].get_color():
                raise IllegalMove
        
        #Check Queen movement for legal moves, diagnoal and straight up to length of the board
        #Represents horizontal    
        if start_row == end_row:
            single_horz = int((end_column - start_column) / abs(end_column - start_column))
            while temp_column!= end_column:
                temp_column += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_column != end_column):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
            
        #Represents vertical            
        if start_column == end_column: 
            single_horz = int((end_row - start_row) / abs(start_row - end_row))
            while temp_row != end_row:
                temp_row += single_horz
                space = self._board[temp_row][temp_column]

                if type(space) != list and (temp_row != end_row):
                    raise IllegalMove
                
            if type(self._board[end_row][end_column]) != list and (temp_row == end_row) and (temp_column == end_column):
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured
            
        #Check diagonal movement    
        if (start_column != end_column) and (start_row != end_row):
            #Horizontal and Vertical should move space spaces, 3 up and 3 left or 3 down and 3 right etc.
            vert_check = abs(start_row - end_row)
            horz_check = abs(end_column - start_column)

            if vert_check != horz_check: #Not moving diagonally
                raise IllegalMove
            
            single_vert = int((end_row - start_row) / abs(start_row - end_row)) #Should return either 1 or +1
            single_horz = int((end_column - start_column) / abs(start_column - end_column))

            while temp_column != end_column and temp_row != end_row:
                temp_column += single_horz
                temp_row += single_vert
                #Check
                space = self._board[temp_row][temp_column]
                #Not on last iteration 

                if type(space) != list and (temp_row != end_row) and (temp_column != end_column):
                    raise IllegalMove
                #on last iteration and not moving, captured piece

            if type(self._board[end_row][end_column]) != list:
                captured = self._board[end_row][end_column] #Captured
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return captured #Piece captured
            
            if type(self._board[end_row][end_column]) == list:
                temp = self._board[start_row][start_column] #Beginning
                self._board[end_row][end_column], self._board[start_row][start_column] = temp, ['']
                return None #none captured

    def pawn_move(self, start, end):
        """
        Pawn Movement function
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken 
        """

        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        if self._board[start_row][start_column].get_color() == 'white':
            piece_taken = self.white_pawn(start, end)
        else:
            piece_taken = self.black_pawn(start, end)
        return piece_taken
    
    def white_pawn(self, start, end):
        """
        White Pawn movement
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken 
        """

        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        #White pawn must move forward
        temp_column, temp_row = start_column, start_row
        lateral = 0
        #Check Legal Moves
        #Check if it is starting from 2nd row and movement
        if start_row == 2:
            total_movement = abs(start_row - end_row) + abs(start_column - end_column)
            #allowing movement for both diagonal capture and two spaces up or one space up
            if total_movement > 2:
                raise IllegalMove
        #Else: Check if it is only moving by one space
        elif abs(end_column - start_column) == 0:
            total_movement = abs(start_row - end_row)
            if total_movement != 1 and start_row != 2:
                raise IllegalMove
        #Total movement moving up and left/right should be equal to 2
        elif abs(end_column - start_column) == 1:
            up_move = abs(start_row - end_row)
            side_move = abs(start_column - end_column)
            #Making sure it's only moving up 1 and to the side by 1
            if up_move != 1 and side_move != 1:
                raise IllegalMove
            #Checking if pawn uses capture move on empty space
            if type(self._board[end_row][end_column]) == list:
                raise IllegalMove
            #Checking if pawn is on same color space
            if self._board[end_row][end_column].get_color() == self._board[start_row][start_column].get_color():
                raise IllegalMove   
        else:
            raise IllegalMove
 
        #Iterate and check if it is bumping anything
        #Moving up 1 or up 2 from row 2 / Capturing up 1 and left/right 1
        while temp_row != end_row:
            temp_row += 1
            #Lateral movement
            if temp_column != end_column:
                lateral = end_column - temp_column
                temp_column += lateral 
            #Check spaces in between
            space = self._board[temp_row][temp_column]
            #Straight movement and runs into not a list
            if type(space) != list and lateral == 0:
                raise IllegalMove
            #Check if capture movement is valid onto empty space
            if type(space) == list and (abs(temp_column - start_column) == 1 and abs(temp_row - start_row) == 1):
                raise IllegalMove

        #Piece Taken
        if type(self._board[end_row][end_column]) != list:
            temp = self._board[start_row][start_column] 
            self._board[start_row][start_column] = ['']
            piece_to_take = self._board[end_row][end_column]
            self._board[end_row][end_column] = temp
            return piece_to_take
        #Piece not Taken
        if type(self._board[end_row][end_column]) == list:
            temp = self._board[start_row][start_column] 
            self._board[start_row][start_column] = ['']
            self._board[end_row][end_column] = temp
            return None
        
    def black_pawn(self, start, end):
        """
        Black Pawn movement
        start = Piece starting point/piece to be used
        end = Piece landing/ending point
        return = Piece Taken 
        """
        start_row = int(start[1])
        start_column = int(ord(start[0]) - 97)

        end_row = int(end[1])
        end_column = int(ord(end[0]) - 97)
        #Black pawn must move backwards
        temp_column, temp_row = start_column, start_row
        lateral = 0
        #Check Legal Moves
        #Check if it is starting from 2nd row and movement
        if start_row == 7:
            total_movement = abs(start_row - end_row) + abs(start_column - end_column)
            #allowing movement for both diagonal capture and two spaces up or one space up
            if total_movement > 2:
                raise IllegalMove
        #Check if it is only moving by one space
        elif abs(end_column - start_column) == 0:
            total_movement = abs(start_row - end_row)
            if total_movement != 1 and start_row != 7:
                raise IllegalMove
        #Total movement moving up and left/right should be equal to 2
        elif abs(end_column - start_column) == 1:
            up_move = abs(start_row - end_row)
            side_move = abs(start_column - end_column)
            #Making sure it's only moving up 1 and to the side by 1
            if up_move != 1 and side_move != 1:
                raise IllegalMove
            #Checking if pawn uses capture move on empty space
            if type(self._board[end_row][end_column]) == list:
                raise IllegalMove
            #Checking if pawn is on same color space
            if self._board[end_row][end_column].get_color() == self._board[start_row][start_column].get_color():
                raise IllegalMove
        else:
            raise IllegalMove
        #All else fails, should be illegal
        
        #Iterate and check if it is bumping anything
        #Moving up 1 or up 2 from row 2 / Capturing up 1 and left/right 1
        while temp_row != end_row:
            temp_row -= 1
            if temp_column != end_column:
                lateral = end_column - temp_column
                temp_column += lateral 
            #Check spaces in between
            space = self._board[temp_row][temp_column]
            #Check if movement is moving past a piece
            if type(space) != list and lateral == 0:
                raise IllegalMove           
            #Check if capture movement is valid onto empty space
            if type(space) == list and (abs(temp_column - start_column) == 1 and abs(temp_row - start_row) == 1):
                raise IllegalMove
            #If moving forward and not horizontally onto a space
            
        #Piece Taken
        if type(self._board[end_row][end_column]) != list:
            temp = self._board[start_row][start_column] 
            self._board[start_row][start_column] = ['']
            piece_to_take = self._board[end_row][end_column]
            self._board[end_row][end_column] = temp
            return piece_to_take
        #Piece not Taken
        if type(self._board[end_row][end_column]) == list:
            temp = self._board[start_row][start_column] 
            self._board[start_row][start_column] = ['']
            self._board[end_row][end_column] = temp
            return None

    def make_move(self, start, end):
        """
        Makes move on chess board
        start = Piece starting point
        end = Piece landing point/ending point
        """
        if self._state != "UNFINISHED":
            return False
        if len(start) > 2:
            return False
        if len(end) > 2:
            return False
        
        func_object = {
            'rook': self.rook_move,
            'queen': self.queen_move,
            'king': self.king_move,
            'pawn': self.pawn_move,
            'knight': self.knight_move,
            'bishop': self.bishop_move,
        }
        #Starting Point
        start = start.lower()
        row = int(start[1])
        column = int(ord(start[0]) - 97)

        #Ending Point
        end = end.lower()

        to_move = self._board[row][column]
        if type(to_move) == list:
            return False
        
        try:
            bool_val = self.valid_move(start)
        except:
            return False

        if bool_val == False:
            return False      

        #Check if space is out of boundary
        try:
            bool_val = self.out_of_bounds(start, end)
        except:
            return False
        if bool_val == False:
            return False

        try:
            #piece to take
            self.func1 = func_object[self._board[row][column].get_piece_type().lower()]
            taken_piece = self.func1(start, end)

            if taken_piece is None:
                self.change_turn()
                return True
            
            taken = taken_piece.get_piece()
            #Update List #TODO
            self.update_list(taken)
            #Change turn
            self.change_turn()
           
            #Update Game State
            if ('white Pawn' not in self._white) or ('white Knight' not in self._white) or ('white Bishop' not in self._white) or ('white Queen' not in self._white) or ('white King' not in self._white) or ('white Rook' not in self._white):
                self.set_state('BLACK_WON')
                return True
            
            if ('black Pawn' not in self._black) or ('black Knight' not in self._black) or ('black Bishop' not in self._black) or ('black Queen' not in self._black) or ('black King' not in self._black) or ('black Rook' not in self._black):
                self.set_state('WHITE_WON')
                return True
        except:
            return False
        
        return True

    def valid_move(self, start):
        """
        Checks valid movement for chess piece to check if it is the ocrrect color
        start = Piece starting point
        end = Piece landing/ending point
        """
        #Splits the string down and sees if it is working
        #Check if space is on the right color
        #OtherPlayerTurn exception
        try:
            row = int(start[1])
            column = int(ord(start[0]) - 97)
            to_move = self._board[row][column] #Which row (1-8), column is a-h
            color = to_move.get_color()
            if color != self._turn:
                raise IncorrectTurn
            return True
        except IncorrectTurn:
            #wrong turn
            print(f"It is {self._turn}'s turn")
            return False
        except:
            #moving empty or something
            print(f"An unknown error occurred and {start} either contains no piece or an invalid entry")
            return False

    def out_of_bounds(self, start, end):
        """
        Checks if movement is out of bounds
        start = Piece starting point
        end = Piece landing/ending point
        """
        start = start.lower()
        row = int(start[1])
        column = int(ord(start[0]) - 97)

        if row > 8 or row < 1:
            return False
        if column < 0 or column > 7:
            return False
        
        end = end.lower()
        row = int(end[1])
        column = int(ord(end[0]) - 97)
        if row > 8 or row < 1:
            return False
        if column < 0 or column > 7:
            return False
        
        return True

    def update_list(self, piece):
        """
        Deletes chess piece from the list of players
        piece = Piece to be deleted from the list
        """
        #white can only take black and black can only take white
        if self._turn == 'white':
            self._black.remove(piece)
        if self._turn == 'black':
            self._white.remove(piece)
        return
    
    def set_state(self, state):
        """
        Updates game state based on the lists of white and black pieces
        state = State of the game
        """
        self._state = state

    def show_turn(self):
        """
        Shows turn of chess color on the board
        """
        return self._turn

    def show_pieces(self, color):
        """
        Shows pieces in list of player and color associated
        color = Color/side of list to be viewed
        """
        color = color.lower()
        if color == "white":
            return self._white
        if color == "black":
            return self._black
        else:
            print("\n")
            print("Invalid color")
            return None