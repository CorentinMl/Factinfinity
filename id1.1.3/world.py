import random
import math

def Init():
	global map
	init_size_x = init_size_x_min, init_size_x_max = -100, 100
	init_size_y = init_size_y_min, init_size_y_max = -100, 100
	map={}
	for x in range (init_size_x_min, init_size_x_max):
		for y in range (init_size_y_min, init_size_y_max):
			GenerateWorld((x,y))
#	print(map[128][128])

def PostInit(background):
	global background_block_x, background_block_y, background_block_x_center, background_block_y_center
	background_block_x = background[0]
	background_block_y = background[1]
	background_block_x_center = background_block_x//2
	background_block_y_center = background_block_y//2

def CalcChunk(player_coords_float, direction):
	global background_block_x, background_block_y, background_block_x_center, background_block_y_center
	player_coords = (math.trunc(player_coords_float[0]), math.trunc(player_coords_float[1]))
	if direction == "north":
		for x in range (player_coords[0]-background_block_x_center-2, player_coords[0]+background_block_x_center+2):
			pos = str(x)+':'+str(player_coords[1]-background_block_y_center-1)
			if not pos in map.keys():
				GenerateWorld((x, player_coords[1]-background_block_y_center-1))
	elif direction == "south":
		for x in range (player_coords[0]-background_block_x_center-2, player_coords[0]+background_block_x_center+2):
			pos = str(x)+':'+str(player_coords[1]+background_block_y_center+1)
			if not pos in map.keys():
				GenerateWorld((x, player_coords[1]+background_block_y_center+1))
	elif direction == "east":
		for y in range (player_coords[1]-background_block_y_center-2, player_coords[1]+background_block_y_center+2):
			pos = str(player_coords[0]+background_block_x_center+1)+':'+str(y)
			if not pos in map.keys():
				GenerateWorld((player_coords[0]+background_block_x_center+1, y))
	elif direction == "west":
		for y in range (player_coords[1]-background_block_y_center-2, player_coords[1]+background_block_y_center+2):
			pos = str(player_coords[0]-background_block_x_center-1)+':'+str(y)
			if not pos in map.keys():
				GenerateWorld((player_coords[0]-background_block_x_center-1, y))

def GetElement(coords):
	global map
	pos = str(coords[0])+':'+str(coords[1])
	return map[pos]

def GenerateWorld(coords):
	global map
	map[str(coords[0])+':'+str(coords[1])]=random.randint(0,1)
