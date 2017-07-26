# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author: Shriya Nandwani
# -----------------------------------------------------------------------------
'''

This program essentially is a Tic Tac Toe game in which a player can compete
against a computer.

'''
import tkinter
import random


class Game(object):
    '''
    This is where the class is defined. The entire game takes place within this
    class.

    Arguments:
    parent

    Attribute:
    self.parent

    '''

    # Add your class variables if needed here - square size, etc...)
    square_size = 150
    square_user_color = 'purple'
    square_computer_color = 'cyan'
    #Default state
    in_progress = True

    def __init__(self, parent):
        '''
        The parent argument is defined and passed in as self.parent, an
        attribute.

        Here, I have created the restart button widget, drawn the board where
        tic tac toe takes place, created a label widget for the win/lose message,
        and lastly, I have intialized the grid.
        '''
        parent.title('Tic Tac Toe')
        # Allow access to parent
        self.parent = parent
        # Create the restart button widget
        self.restart_button = tkinter.Button(self.parent, text = 'restart',
                                        width=20,
                                        command = self.restart)
        # register with the geometry widget
        self.restart_button.grid()
        # Create a canvas widget
        # This also assigns self.my_canvas
        self.draw_board()
        # Create a label widget for the win/lose message
        self.status_label = tkinter.Label(self.parent, text="This is tic tac toe")
        #register with geometry object
        self.status_label.grid()
        # Initialize the grid
        self.my_grid = []
        self.init_grid()

    def restart(self):
        '''
        This method is invoked when the user clicks on the restart button.

        It intializes the game and sets in the progress flag.
        '''
        # This method is invoked when the user clicks on the RESTART button.
        self.status_label.configure(text="Restart was invoked")
        #initialize the game
        self.init_grid()
        #Set the in_progress flag
        self.in_progress = True

    def play(self, event):
        '''
        When the user clicks on a square, this method is invoked. A square will
        appear in response to the move the player wants to make and a
        response will be made by the computer.

        If the game is complete or there are no moves left, it will not have a
        computer response or allow the square the player has selected to output
        a tic tac toe move.

        '''
        # This method is invoked when the user clicks on a square.
        # Return right away if the game is complete
        if self.in_progress == False:
            return

        self.column = event.x // self.square_size
        self.row = event.y // self.square_size
        #  if square is empty set the value of the square
        # otherwise return without doing anything
        if (self.play_square(self.row, self.column, 'User') == False):
            return
        shape = self.my_canvas.find_closest(event.x, event.y)
        self.my_canvas.itemconfigure(shape, fill=self.square_user_color)
        result = self.evaluate_game(self.my_grid)
        self.set_game_status(result)
        if (result == 'In_Progress'):
            self.play_computer()
        else:
            #Looks like we are in state where we need a reset
            self.in_progress = False




    def play_computer(self):
        '''

        '''
        index = self.find_optimal_move()
        self.my_grid[index] = 'Computer'
        self.my_canvas.itemconfigure((index+1,),
                                     fill=self.square_computer_color)
        result = self.evaluate_game(self.my_grid)
        self.set_game_status(result)
        if (result != 'In_Progress'):
            self.in_progress = False

    def set_game_status(self, result):
        if (result == 'User'):
            self.status_label.configure(text= 'You won!')
        elif (result == 'Computer'):
            self.status_label.configure(text='You lost!')
        elif (result == 'Tie'):
            self.status_label.configure(text="It's a tie!")
        else:
            self.status_label.configure(text="In Progress")

    #finds the  winning move for the computer if possible
    #if found returns the winning index else finds the best
    #defensive move. If no defensive move is also found, returns the first random move
    def find_optimal_move(self):
        count = 0
        my_grid_copy = self.my_grid
        while (count < 9):
            if (my_grid_copy[count] == 'None'):
                my_grid_copy[count] = 'Computer'
                #check if this is a winning move
                if(self.evaluate_game(my_grid_copy) == 'Computer'):
                    #This is a winning move!
                    return count
                else:
                    #reset the grid
                    my_grid_copy[count] = 'None'
            count = count + 1
        # if we are here, we didn't find a winning move
        # let's see if we can find the best defensive move
        count = 0
        while (count < 9):
            if (my_grid_copy[count] == 'None'):
                my_grid_copy[count] = 'User'
                # check if this is a winning move for the user
                if (self.evaluate_game(my_grid_copy) == 'User'):
                    # This is a winning move for the user
                    # We must play here as defense
                    return count
                else:
                    # reset the grid
                    my_grid_copy[count] = 'None'
            count = count + 1
        # if we are here, no winning move was found
        # we also don't have an imminent danger of losing
        # let's do a random move
        index = random.randint(0, 8)
        while (self.my_grid[index] != 'None'):
            index = random.randint(0, 8)
        return index




    # evaluates the game and returns appropriate result
    def evaluate_game(self, grid):
        #winning combinations
        #any column is consistent
        for row in range(3):
            # All rows match
            if ( (grid[row*3] == grid[row*3+1]) and
                     (grid[row*3] == grid[row*3+2]) ):
                if (grid[row*3] != 'None'):
                    return grid[row*3]

        # All Columns match
        for column in range(3):
            if ( (grid[column] == grid[column+3]) and
                     (grid[column] == grid[column+6])):
                if (grid[column] != 'None'):
                    return grid[column]

        # L to R diagnol matches
        if( (grid[0] != 'None') and
                (grid[0] == grid[4]) and
                (grid[0] == grid [8])):
            return grid[0]

        # R to L diagnol match
        if ( (grid[2] != 'None') and
                 (grid[2] == grid[4]) and
                 (grid[2] == grid[6])):
            return grid[2]

        #In Progress, if there's an empty slot
        for index in range(9):
            if grid[index] == 'None':
                return 'In_Progress'

        # If we are here, no more moves are possible, it is a Tie

        return 'Tie'
    # a move was made on a square as a user or the computer
    # Takes the square coordinates and user as input
    # Updates the grid appropriately only updates if the square is unoccupied
    # return True on successful update else False
    def play_square(self, row, column, user):
        index = row * 3 + column
        # if square is empty update it
        if self.my_grid[index] == 'None':
            self.my_grid[index] = user
            return True
        else:
            return False




    def draw_board(self):
        self.my_canvas = tkinter.Canvas(self.parent, width=self.square_size * 3,
                                   height=self.square_size * 3)
        # register it with geometry manager
        self.my_canvas.grid()
        self.my_canvas.bind("<Button-1>", self.play)
        # Draw the squares on the board
        for row in range(3):
            for column in range(3):
                my_rect = self.my_canvas.create_rectangle(self.square_size*column,
                                             self.square_size*row,
                                             self.square_size* (column+1),
                                             self.square_size*(row+1),
                                             fill='white')
    #initialize the grid data structure
    #'None' indicates current occupier is 'None'
    #Also resets color of the Grid
    def init_grid(self):

        i = 0
        self.my_grid = []
        for i in range(9):
            self.my_grid.append('None')
        for shape in self.my_canvas.find_all():
            self.my_canvas.itemconfigure(shape, fill='White')



def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    my_game = Game(root)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()