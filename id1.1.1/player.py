import pygame
import world as World
import math
#player_texture, player_screen_coords, player_direction

DIAGONAL_LONG = 1/(math.sqrt(2))
DIR_NORTH = 0
DIR_NORTH_EAST = 1
DIR_EAST = 2
DIR_SOUTH_EAST = 3
DIR_SOUTH = 4
DIR_SOUTH_WEST = 5
DIR_WEST = 6
DIR_NORTH_WEST = 7

def Init(screen_size):
	global is_player_moving, player_speed, player_texture, player_screen_coords, player_direction, player_size, player_size_x, player_size_y, player_coords, player_x_coord, player_y_coord
	#Initialisation des ressources
	player_texture = pygame.image.load("../../res/textures/player/player-idle.png")
	player_size = player_size_x, player_size_y = 92, 116
	player_screen_coords = player_x_screen_coord, player_y_screen_coord = (screen_size[0]-player_size_x)/2, (screen_size[1]-player_size_y)/2
	player_coords = player_x_coord, player_y_coord = 0.0, 0.0
	player_direction = 0
	is_player_moving = False
	player_speed = 0.1

def EventManager(event): #Event de pygame
	global player_x_coord, player_y_coord, is_player_moving
	if event.type == pygame.KEYDOWN:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			ChangeDirection(event.key)


			if event.key == pygame.K_UP:
				player_y_coord -= 0.5
				World.CalcChunk((player_x_coord, player_y_coord), "north")
			elif event.key == pygame.K_RIGHT:
				player_x_coord += 0.5
				World.CalcChunk((player_x_coord, player_y_coord), "east")
			elif event.key == pygame.K_DOWN:
				player_y_coord += 0.5
				World.CalcChunk((player_x_coord, player_y_coord), "south")
			elif event.key == pygame.K_LEFT:
				player_x_coord -= 0.5
				World.CalcChunk((player_x_coord, player_y_coord), "west")

	elif event.type == pygame.KEYUP:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):


def Move():
	if is_player_moving:
		if player_direction == DIR_NORTH:
			player_y_coord -= player_speed
		elif player_direction == DIR_NORTH_EAST:
			player_y_coord -= player_speed*DIAGONAL_LONG
			player_x_coord += player_speed*DIAGONAL_LONG
		elif player_direction == DIR_EAST:
			player_x_coord += player_speed
		elif player_direction == DIR_SOUTH_EAST:
			player_y_coord += player_speed*DIAGONAL_LONG
			player_x_coord += player_speed*DIAGONAL_LONG
		elif player_direction == DIR_SOUTH:
			player_y_coord += player_speed
		elif player_direction == DIR_SOUTH_WEST:
			player_y_coord += player_speed*DIAGONAL_LONG
			player_x_coord -= player_speed*DIAGONAL_LONG
		elif player_direction == DIR_WEST:
			player_x_coord -= player_speed
		elif player_direction == DIR_NORTH_WEST:
			player_y_coord -= player_speed*DIAGONAL_LONG
			player_x_coord -= player_speed*DIAGONAL_LONG


def ChangeDirection(key, type): #Touche du clavier (direction)
	global player_direction, is_player_moving
	if type == "KEYDOWN":
		if is_player_moving:
			if key == pygame.K_UP:
				if player_direction == DIR_EAST:
					player_direction == DIR_NORTH_EAST
				elif player_direction == DIR_WEST:
					player_direction = DIR_NORTH_WEST
				else:
					player_direction = DIR_NORTH
			elif key == pygame.K_RIGHT:
				if player_direction == DIR_NORTH:
					player_direction == DIR_NORTH_EAST
				elif player_direction == DIR_SOUTH:
					player_direction = DIR_SOUTH_EAST
				else:
					player_direction = DIR_EAST
			elif key == pygame.K_DOWN:
				if player_direction == DIR_EAST:
					player_direction == DIR_SOUTH_EAST
				elif player_direction == DIR_WEST:
					player_direction = DIR_SOUTH_WEST
				else:
					player_direction = DIR_SOUTH
			elif key == pygame.K_LEFT:
				if player_direction == DIR_NORTH:
					player_direction == DIR_NORTH_WEST
				elif player_direction == DIR_SOUTH:
					player_direction = DIR_SOUTH_WEST
				else:
					player_direction = DIR_WEST
		else:
			if key == pygame.K_UP:
				player_direction = DIR_NORTH
			elif key == pygame.K_RIGHT:
				player_direction = DIR_EAST
			elif key == pygame.K_DOWN:
				player_direction = DIR_SOUTH
			elif key == pygame.K_LEFT:
				player_direction = DIR_WEST
		is_player_moving = True
	elif type == "KEYUP":
		if key == pygame.K_UP:
			if player_direction == DIR_EAST:
				player_direction == DIR_NORTH_EAST
			elif player_direction == DIR_WEST:
				player_direction = DIR_NORTH_WEST
			else:
				player_direction = DIR_NORTH
		elif key == pygame.K_RIGHT:
			if player_direction == DIR_NORTH:
				player_direction == DIR_NORTH_EAST
			elif player_direction == DIR_SOUTH:
				player_direction = DIR_SOUTH_EAST
			else:
				player_direction = DIR_EAST
		elif key == pygame.K_DOWN:
			if player_direction == DIR_EAST:
				player_direction == DIR_SOUTH_EAST
			elif player_direction == DIR_WEST:
				player_direction = DIR_SOUTH_WEST
			else:
				player_direction = DIR_SOUTH
		elif key == pygame.K_LEFT:
			if player_direction == DIR_NORTH:
				player_direction == DIR_NORTH_WEST
			elif player_direction == DIR_SOUTH:
				player_direction = DIR_SOUTH_WEST
			else:
				player_direction = DIR_WEST




def Display(screen):
	global player_screen_coords, player_texture, player_direction, player_size, player_size_x, player_size_y
	screen.blit(player_texture, player_screen_coords, pygame.Rect((0,player_direction*player_size_y),player_size))

def GetAbsoluteCoords():
	global player_x_coord, player_y_coord
	return (math.trunc(player_x_coord), math.trunc(player_y_coord))

def GetDecimalCoords():
	global player_x_coord, player_y_coord
	return (player_x_coord-math.trunc(player_x_coord), player_y_coord-math.trunc(player_y_coord))
