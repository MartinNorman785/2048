"""
Module that holds the Grid Class
"""



import random


class Grid():
  """
  Class that holds and alters the grid of 2048

  Variables
  --------------------
  tiles: List of Lists
    Holds values of each of the 16 tiles. 
    Empty values set to 1

  state: string
    The state that the game is in
    either [cont] for continous [won] for a won game
    or [lost] for a lost game
  
  Methods
  -------------------
  score()
    Returns the sum of all the tiles on the board
  
  add_tile(tile=None)
    Add a random tile to the grid if no argument otherwise the tile given
    
  move_all(direction)
    Moves all the tiles in the given direction
    
  check_won()
    Returns True if there is a 2048 on the board else False
    
  place_tile(index, tile)
    Places the tile given based on the index given skipping filled locations
  """

  
  def __init__(self):
    '''Defines the grid and adds the two starting tiles randomly'''

    
    # Initialising the grid
    self.tiles = [
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None],
    ]

    self.state = "cont"

    #Getting the two starting tiles
    self.add_tile(2)
    self.add_tile(2)
    

  
  def __str__(self):
    """What the grid returns when printed"""
    string = ""
    for row in self.tiles:
      for tile in row:
        string = string + str(tile) + " "*(5-len(str(tile)))
      string = string + "\n"
    return string

  def score(self):
    """Returns the sum of all tiles on the board."""
    count = 0
    for row in self.tiles:
      for i in row:
        if i is not None:
          count += i
    return count
  

  def add_tile(self, tile=None) -> None:
    """
    Add a random tile to the grid if no argument otherwise the tile given

    Parameters
    ---------------
    tile=None: int
      Value placed on the grid
      If None gives it a random choice
    
    """

    
    # If their is a not a specific choice of tile choose one randomly from list [2, 2, 4]
    if tile is None:
      tile = random.choice([2,2,4])

    # Getting all the spare tiles
    left = self.tiles_spare()
    # Getting a random index of the free spots to place the tile at
    tile_index = random.choice(list(range(left)))
    #Placing the tile chosen at that index
    self.place_tile(tile_index, tile)


  
  def move_all(self, direction: str) -> None:
    """
    Moves all the tiles in the given direction
    
    Parameters
    ---------------
    direction: str
      A value that is either UP, DOWN, RIGHT or LEFT
      Will be used to make desicsions of how to move grid
    """


    
    if direction == 'UP' or direction == 'DOWN': # Moving columns
      # Creating a new grid to assign values to
      new_grid = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
      ]


      # Looping for each of the columns
      for i in range(4):
        # Initialising the new column
        new_column = []

        #Getting the original column from the grid
        column = [x[i] for x in self.tiles]

        # Adding the tiles that are not None in column to the new column
        for tile in column:
          if tile is not None:
             new_column.append(tile)


        # Merging all the items in the column if the same
        new_column = self.join_when_move(new_column)

        

        # Filling out the list with the remaining Nones for emtpty slots
        while len(new_column) < 4:
          if direction == 'DOWN':
            new_column = [None] + new_column
          else:
            new_column.append(None)

        # Adding the column to the new grid
        for x in range(len(new_column)):
          new_grid[x][i] = new_column[x]
 
    else: # Moving the grid along the rows
      # Intialising the new grid
      new_grid = []

      # Looping through each of the rows in the grid
      for i in range(4):

        # Intialsing the new row
        new_row = []

        # Adding the tile to the new row if it is not equal to None or empty
        for tile in self.tiles[i]:
          if tile is not None:
             new_row.append(tile)


        # Merging all of the tiles in the row if their are the same
        new_row = self.join_when_move(new_row)

        # Adding empty values or None to fill out the list
        while len(new_row) < 4:
          if direction == 'RIGHT':
            new_row = [None] + new_row
          else:
            new_row.append(None)

        # Adding the new row to the grid
        new_grid.append(new_row)
    # If their is a change to the grid; Don't want to add a tile if no move
    if new_grid != self.tiles: 
      # Setting the new grid as the main grid
      self.tiles = new_grid
  
      # Adding a random tile to the grid after each move
      self.add_tile()
    return
      



  def check_won(self) -> bool:
    """Returns True if there is a 2048 on the board otherwise False"""
    for row in self.tiles:
      for tile in row:
        
        if tile == 2048:
          return True
          
    return False

  def check_lost(self) -> bool:
    """Returns True if there is no moves that do anyting otherwise False"""
    # Creating an instance of the grid to check if their is a move and to revert
    grid = self.tiles.copy()

    # For each of the possible moves
    for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:

      # Checking the move
      self.move_all(direction)

      # If the moved version is the not the same as the original
      if self.tiles != grid:

        # Reverting the grid to the original
        self.tiles = grid
        
        return False
      
    return True
    
  

  def tiles_spare(self) -> int:
    """Returns the number of empty tiles"""
    n = 0
    for row in self.tiles:
      for tile in row:
        if tile is None:
          n += 1
    return n

  
  def place_tile(self, index: int, val: int) -> None:
    """
    Places the tile given based on the index given skipping filled locations

    Parameters
    ------------
    index: int
      Used as the index to place the tile at not including filled locations
    val: int
      The value that will be placed in the location

    Changes
    ------------
    self.tiles
      changes the value at the index with skipped filled locations to the val given
    """
    
    i = 0

    # Looping through all of the tiles in the grid
    for r, row in enumerate(self.tiles):
      for t, tile in enumerate(row):

        # If the tile is Empty (None) check and increase otherwise skip
        if tile is None:

          # If correct tile index
          if index == i:
            
            self.tiles[r][t] = val
            return

          # Increasing the count of tiles gone over
          i += 1
    return
    


  def join_when_move(self, list: list) -> list:
    """
    Returns a new list for moving that where the same elements are merged
    if they are next to each other

    Parameters
    ---------------
    list: list
      A list of the row or column being moved that will be merged

    Returns:
    new: list
      The merged list
    """

    
    # Returns an empty list if an empty list is given
    if list == []:
      return []

    # Intialsing a new list
    new = []

    # Looping through the list to merge all in list or add
    for i in range(len(list)):

      if new != [] and list[i] == new[-1]: # If same to merge
        # Removing the last from the list
        new = new[:-1]
        # Adding the new that is double the previous
        new.append(str(list[i]*2))
      else: # Adding normally
        new.append(list[i])
    return [int(x) for x in new]


  def grid_reset(self):
    self.state = "cont"
    self.tiles = [
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None]
    ]
    self.add_tile(2)
    self.add_tile(2)
    
    
