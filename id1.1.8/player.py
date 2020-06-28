import pygame
import world as World
import math
import background as Background
import database as Database
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

def CalcInit():
	global player_move_direction, is_player_moving, player_speed, player_direction, player_coords, player_x_coord, player_y_coord
	load_data = Database.LoadPlayer()
	if load_data:
		player_coords = player_x_coord, player_y_coord = load_data[2], load_data[3]
		player_move_direction = load_data[4]
		player_speed = load_data[5]
	else:
		player_coords = player_x_coord, player_y_coord = 0.0, 0.0
		player_move_direction = DIR_NORTH
		player_speed = 0.25 #cases/tick
	player_direction = [False, False, False, False, False, False, False, False]
	is_player_moving = False




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
	global player_direction, is_player_moving, player_move_direction, running_state
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
		running_state = 0
		is_player_moving = False
	else:
		is_player_moving = True

def Teleport(x, y):
	global player_x_coord, player_y_coord
	player_x_coord, player_y_coord = x, y
	World.LoadWorldAroundPostition((int(x), int(y)), 50)
	Background.CalcPositions()

def GetAbsoluteCoords():
	global player_x_coord, player_y_coord
	return (math.trunc(player_x_coord), math.trunc(player_y_coord))

def GetDecimalCoords():
	global player_x_coord, player_y_coord
	return (player_x_coord-math.trunc(player_x_coord), player_y_coord-math.trunc(player_y_coord))

def GetData():
	return ((player_x_coord, player_y_coord, player_move_direction, player_speed))

#
#							FPS
#

def DisplayInit(screen_size):
	global player_texture, player_size, player_screen_coords, player_x_screen_coord, player_y_screen_coord, running_state, running_max_states
	player_texture = [pygame.image.load("../../res/textures/player/player-idle.png"), pygame.image.load("../../res/textures/player/player-running.png")]
	running_max_states = 21
	running_state = 0
	player_size = [(92, 116), (88, 132)]
	player_screen_coords = player_x_screen_coord, player_y_screen_coord = (screen_size[0]-player_size[0][0])/2, (screen_size[1]-player_size[0][1])/2


def Display(screen):
	global player_screen_coords, player_direction, player_size, running_state
	if is_player_moving:
		screen.blit(player_texture[1], player_screen_coords, pygame.Rect((math.floor(running_state)*player_size[1][0],player_move_direction*player_size[1][1]),player_size[1]))
		running_state += 0.75
		if running_state > running_max_states:
			running_state = 0
	else:
		screen.blit(player_texture[0], player_screen_coords, pygame.Rect((0,player_move_direction*player_size[0][1]),player_size[0]))
