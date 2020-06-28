import pygame
#player_texture, player_screen_coords, player_direction

def Init(screen_size):
	global player_texture, player_screen_coords, player_direction, player_size, player_size_x, player_size_y, player_coords, player_x_coord, player_y_coord
	#Initialisation des ressources
	player_texture = pygame.image.load("../../res/textures/player/player-idle.png")
	player_size = player_size_x, player_size_y = 92, 116
	player_screen_coords = player_x_screen_coord, player_y_screen_coord = (screen_size[0]-player_size_x)/2, (screen_size[1]-player_size_y)/2
	player_coords = player_x_coord, player_y_coord = 128, 128
	player_direction = 0

def EventManager(event): #Event de pygame
	global player_x_coord, player_y_coord
	if event.type == pygame.KEYDOWN:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			ChangeDirection(event.key)
			if event.key == pygame.K_UP:
				player_y_coord -= 1
			elif event.key == pygame.K_RIGHT:
				player_x_coord += 1
			elif event.key == pygame.K_DOWN:
				player_y_coord += 1
			elif event.key == pygame.K_LEFT:
				player_x_coord -= 1

def ChangeDirection(direction): #Touche du clavier (direction)
	global player_direction
	if direction == pygame.K_UP:
		player_direction = 0
	elif direction == pygame.K_RIGHT:
		player_direction = 2
	elif direction == pygame.K_DOWN:
		player_direction = 4
	elif direction == pygame.K_LEFT:
		player_direction = 6

def Display(screen):
	global player_screen_coords, player_texture, player_direction, player_size, player_size_x, player_size_y
	screen.blit(player_texture, player_screen_coords, pygame.Rect((0,player_direction*player_size_y),player_size))

def GetCoords():
	global player_x_coord, player_y_coord
	return (player_x_coord, player_y_coord)
