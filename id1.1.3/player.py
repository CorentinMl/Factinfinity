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
	global player_move_direction, is_player_moving, player_speed, player_texture, player_screen_coords, player_direction, player_size, player_size_x, player_size_y, player_coords, player_x_coord, player_y_coord
	#Initialisation des ressources
	player_texture = pygame.image.load("../../res/textures/player/player-idle.png")
	player_size = player_size_x, player_size_y = 92, 116
	player_screen_coords = player_x_screen_coord, player_y_screen_coord = (screen_size[0]-player_size_x)/2, (screen_size[1]-player_size_y)/2
	player_coords = player_x_coord, player_y_coord = 0.0, 0.0
	player_direction = [False, False, False, False, False, False, False, False]
	player_move_direction = DIR_NORTH
	is_player_moving = False
	player_speed = 0.25 #cases/tick


def Move():
	global player_x_coord, player_y_coord
	old_x, old_y = player_x_coord, player_y_coord
	if is_player_moving:
		if player_move_direction == DIR_NORTH:
			player_y_coord -= player_speed
		elif player_move_direction == DIR_NORTH_EAST:
			player_y_coord -= player_speed*DIAGONAL_LONG
			player_x_coord += player_speed*DIAGONAL_LONG
		elif player_move_direction == DIR_EAST:
			player_x_coord += player_speed
		elif player_move_direction == DIR_SOUTH_EAST:
			player_y_coord += player_speed*DIAGONAL_LONG
			player_x_coord += player_speed*DIAGONAL_LONG
		elif player_move_direction == DIR_SOUTH:
			player_y_coord += player_speed
		elif player_move_direction == DIR_SOUTH_WEST:
			player_y_coord += player_speed*DIAGONAL_LONG
			player_x_coord -= player_speed*DIAGONAL_LONG
		elif player_move_direction == DIR_WEST:
			player_x_coord -= player_speed
		elif player_move_direction == DIR_NORTH_WEST:
			player_y_coord -= player_speed*DIAGONAL_LONG
			player_x_coord -= player_speed*DIAGONAL_LONG
		x_diff = math.trunc(old_x) - math.trunc(player_x_coord)
		if x_diff > 0:
				World.CalcChunk((player_x_coord, player_y_coord), "west")
		elif x_diff < 0:
				World.CalcChunk((player_x_coord, player_y_coord), "east")
		y_diff = math.trunc(old_y) - math.trunc(player_y_coord)
		if y_diff > 0:
			World.CalcChunk((player_x_coord, player_y_coord), "north")
		elif y_diff < 0:
			World.CalcChunk((player_x_coord, player_y_coord), "south")

def ChangeDirection(key, type): #Touche du clavier (direction)
	move_x = 0
	move_y = 0
	global player_direction, is_player_moving, player_move_direction
	if type == "KEYDOWN":
		if key == pygame.K_UP:
			player_direction[DIR_NORTH] = True
		elif key == pygame.K_RIGHT:
			player_direction[DIR_EAST] = True
		elif key == pygame.K_DOWN:
			player_direction[DIR_SOUTH] = True
		elif key == pygame.K_LEFT:
			player_direction[DIR_WEST] = True
	elif type == "KEYUP":
		if key == pygame.K_UP:
			player_direction[DIR_NORTH] = False
		elif key == pygame.K_RIGHT:
			player_direction[DIR_EAST] = False
		elif key == pygame.K_DOWN:
			player_direction[DIR_SOUTH] = False
		elif key == pygame.K_LEFT:
			player_direction[DIR_WEST] = False

	if player_direction[DIR_NORTH]:
		move_y -= 1
	if player_direction[DIR_EAST]:
		move_x += 1
	if player_direction[DIR_SOUTH]:
		move_y += 1
	if player_direction[DIR_WEST]:
		move_x -= 1

	if move_x == 0 and move_y == 1:
		player_move_direction = DIR_SOUTH
	elif move_x == 1 and move_y == 0:
		player_move_direction = DIR_EAST
	elif move_x == 0 and move_y == -1:
		player_move_direction = DIR_NORTH
	elif move_x == -1 and move_y == 0:
		player_move_direction = DIR_WEST

	if move_x == 1 and move_y == 1:
		player_move_direction = DIR_SOUTH_EAST
	elif move_x == 1 and move_y == -1:
		player_move_direction = DIR_NORTH_EAST
	elif move_x == -1 and move_y == 1:
		player_move_direction = DIR_SOUTH_WEST
	elif move_x == -1 and move_y == -1:
		player_move_direction = DIR_NORTH_WEST


	if move_x == 0 and move_y == 0:
		is_player_moving = False
	else:
		is_player_moving = True


def Display(screen):
	global player_screen_coords, player_texture, player_direction, player_size, player_size_x, player_size_y
	screen.blit(player_texture, player_screen_coords, pygame.Rect((0,player_move_direction*player_size_y),player_size))

def GetAbsoluteCoords():
	global player_x_coord, player_y_coord
	return (math.trunc(player_x_coord), math.trunc(player_y_coord))

def GetDecimalCoords():
	global player_x_coord, player_y_coord
	return (player_x_coord-math.trunc(player_x_coord), player_y_coord-math.trunc(player_y_coord))
