import pygame

import colours

pygame.init()
font_for_tiles = pygame.font.SysFont("dejavusans", 35, True)
font_for_score = pygame.font.SysFont("dejavuserif", 50, False)

tile_colours = {
  2: colours.WHITE,
  4: colours.SILVER,
  8: colours.LIGHTGRAY,
  16: colours.LIGHTYELLOW,
  32: colours.YELLOW,
  64: colours.GOLD,
  128: colours.ORANGE,
  256: colours.ORANGERED,
  512: colours.RED,
  1024: colours.PURPLE,
  2048: colours.BLUE,
  4096: colours.GREEN,
  8192: colours.CYAN,
  16384: colours.LIME,
  32768: colours.MAGENTA
}

def draw_main(win, grid):
  # Background recreation
  win.fill(colours.BEIGE)

  # Drawing the main grid
  pygame.draw.rect(win, colours.BLACK, (125, 125, 450, 450), 0)

  # Drawing the smaller 4 tiles
  for r in range(4):
    for c in range(4):
      if grid.tiles[c][r] is not None:
        pygame.draw.rect(win, tile_colours[grid.tiles[c][r]], (135+r*110, 135+c*110, 100, 100), 0)
        text = font_for_tiles.render(str(grid.tiles[c][r]), True, colours.BLACK)
        width = text.get_width()
        height = text.get_height()
        win.blit(text, (185+r*110-width/2, 185+c*110 - height/2))
      else:
        pygame.draw.rect(win, colours.GREY, (135+r*110, 135+c*110, 100, 100), 0)


  # Drawing the state of the board
  if grid.state == "cont":
    text = font_for_score.render(f"Score: {grid.score()}", True, colours.BLACK)
  elif grid.state == "won":
    text = font_for_score.render(f"You won. Score: {grid.score()}", True, colours.BLACK)
  else:
    text = font_for_score.render(f"You lost. Score: {grid.score()}", True, colours.BLACK)
  width = text.get_width()
  height = text.get_height()
  win.blit(text, (win.get_width()/2-width/2, 100 - height/2))
