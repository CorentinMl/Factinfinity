import pygame
import random
import player as Player
import world as World

def Init(screen_size):
	global background_blocks, background_texture, background_width, background_height, background_screen, background_center_x, background_center_y
	background_texture = [pygame.image.load("../../res/textures/background/dirt-1.png"),pygame.image.load("../../res/textures/background/grass-1.png")]
	background_blocks = background_width, background_height = int(screen_size[0]//(background_texture[0].get_width())+1), int(screen_size[1]//(background_texture[0].get_height())+1)
	background_screen = pygame.Surface(screen_size)
	background_center = background_center_x, background_center_y = background_width//2, background_height//2
	CalcPositions()

def EventManager(event): #Event de pygame
	if event.type == pygame.KEYDOWN:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			CalcPositions()

def CalcPositions():
	global background_width, background_height, background_screen, background_center_x, background_center_y
	#print(World.GetElement(Player.GetCoords()))
	player_coords = Player.GetAbsoluteCoords()
	player_decimal_coords = Player.GetDecimalCoords()
	#print(player_decimal_coords)
	for x in range (-1, background_width+1):
		for y in range (-1, background_height+1):
			background_screen.blit(background_texture[World.GetElement((x+player_coords[0]-background_center_x,y+player_coords[1]-background_center_y))], ((x-player_decimal_coords[0])*background_texture[0].get_width(),(y-player_decimal_coords[1])*background_texture[0].get_height()))

def Display(screen):
	global background_screen
	screen.blit(background_screen, (0, 0))

def GetBackgroundBlockNumber():
	global background_blocks
	return background_blocks
