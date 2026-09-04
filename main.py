"""
The main script code for the game 2048

This will play the game 2048 using pygame
The user will be able to move a 4x4 grid of tiles using the arrow keys
If the two of the same tiles hit each other during a move they will merge and double
After every move a new tile will spawn randomly into the grid
The aim is to get a tile with value 2048 on the grid
The user will lose if all the tiles are full
and their are no possible moves where a merge can be made

The user will be able to activate an AI
The AI has been trained and continue to be trained with a saved training
The AI is able to find the best or close to best possible moves.


The script can be run or used as a module

If used as a module the main() function should be used
this will require a pygame window
"""


import pygame

from button import Button
import colours
import window
from grid import Grid


def main(win):
  """
  The python script for running the game 2048 in python


  Will both play 2048 and have the option of implementing the AI

  Paramaters
  ----------------
  win: Pygame Display
    A pygame display that is set to size (700, 700)
    Will be used to display the output of the game
  """

  # Initialising pygame
  pygame.init()
  
  # Initililising the grid
  grid = Grid()


  # Initialsing the buttons on the grid
  buttons = [
    Button(50, 20, 50, 200, "New Game", colours.GRAY, lambda: grid.grid_reset())
  ]
  
  # Main loop
  run = True
  while run:

    window.draw_main(win, grid)


    for button in buttons:
      button.draw(win)
      
    
    # Checking for user input
    for event in pygame.event.get():
      
      # If pygame is closed
      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        run = False
        pygame.quit()
        
      # If a location is pressed
      if event.type == pygame.MOUSEBUTTONDOWN:
        mousepos = pygame.mouse.get_pos()
        for button in buttons:
          button.check_pressed(button, mousepos[0], mousepos[1])
        
      # A key is pressed down
      if event.type == pygame.KEYDOWN:

        # If an arrow key is pressed move grid in that direction
        
        if event.key == pygame.K_UP: # Up key; Move up
          grid.move_all("UP")


        if event.key == pygame.K_RIGHT: # Right key; Move right
          grid.move_all("RIGHT")

        
        if event.key == pygame.K_LEFT: # Left key; Move left
          grid.move_all("LEFT")

        
        if event.key == pygame.K_DOWN: # Down key; Move down
          grid.move_all("DOWN")


    # If the user won
    if grid.check_won():
      grid.state = 'won'

    # If the user lost
    elif grid.check_lost():
      grid.state = 'lost'


      
    

    # Processing the updates to the display
    pygame.display.update()
  pygame.quit()



if __name__ == "__main__":
  
  # Initialising a pygame window
  pygame.init()
  win = pygame.display.set_mode((700,700))


  # Running the main code
  main(win)
  

