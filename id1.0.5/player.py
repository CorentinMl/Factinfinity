import pygame
#player_texture, player_coords, player_direction

def Init(screen_size):
	global player_texture, player_coords, player_direction
	#Initialisation des ressources
	player_texture = [pygame.image.load("../../res/textures/player/player-idle-north.png"),pygame.image.load("../../res/textures/player/player-idle-east.png"),pygame.image.load("../../res/textures/player/player-idle-south.png"),pygame.image.load("../../res/textures/player/player-idle-west.png")]
	#Initialisation des coordonées du joueur:
	player_coords = player_x_coord, player_y_coord = (screen_size[0]-player_texture[0].get_width())/2, (screen_size[1]-player_texture[0].get_width())/2
	player_direction = 0

def EventManager(event): #Event de pygame
	if event.type == pygame.KEYDOWN:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			ChangeDirection(event.key)


def ChangeDirection(direction): #Touche du clavier (direction)
	global player_direction
	if direction == pygame.K_UP:
		player_direction = 0
	elif direction == pygame.K_RIGHT:
		player_direction = 1
	elif direction == pygame.K_DOWN:
		player_direction = 2
	elif direction == pygame.K_LEFT:
		player_direction = 3

def Display(screen):
	global player_coords, player_texture, player_direction
	screen.blit(player_texture[player_direction], player_coords)
