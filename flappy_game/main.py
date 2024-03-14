import pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
BG_COLOR = (255,255,255) 
PLAYER_COLOR = (255,0,0)
PLAYER_SIZE = 50
START_X = 200
START_Y = 300
SPEED = 2

pygame.init()
canvas = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
player = pygame.Rect(START_X,START_Y,PLAYER_SIZE,PLAYER_SIZE)

exit = False
while not exit:
  canvas.fill(BG_COLOR)
  pygame.draw.rect(canvas,PLAYER_COLOR,player)

  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT]:
    player.move_ip(-SPEED,0)
  if key[pygame.K_RIGHT]:
    player.move_ip(SPEED,0)
  if key[pygame.K_UP]:
    player.move_ip(0,-SPEED)
  if key[pygame.K_DOWN]:
    player.move_ip(0,SPEED)
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit = True
        
  pygame.display.update()

pygame.quit()