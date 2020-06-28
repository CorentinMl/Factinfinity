import random

def Init():
	global map
	map_size = map_size_x, map_size_y = 256, 256
	map={}
	for x in range (map_size_x):
		for y in range (map_size_y):
			GenerateWorld((x,y))
#	print(map[128][128])

def PostInit(background):
	global background_block_x, background_block_y, background_block_x_center, background_block_y_center
	background_block_x = background[0]
	background_block_y = background[1]
	background_block_x_center = background_block_x//2
	background_block_y_center = background_block_y//2

def CalcChunk(player_coords, direction):
	global background_block_x, background_block_y, background_block_x_center, background_block_y_center
	if direction == "north":
		for x in range (player_coords[0]-background_block_x_center-1, player_coords[0]+background_block_x_center+1):
			pos = str(x)+':'+str(player_coords[1]-background_block_y_center)
			if not pos in map.keys():
				GenerateWorld((x, player_coords[1]-background_block_y_center))
	elif direction == "south":
		for x in range (player_coords[0]-background_block_x_center-1, player_coords[0]+background_block_x_center+1):
			pos = str(x)+':'+str(player_coords[1]+background_block_y_center)
			if not pos in map.keys():
				GenerateWorld((x, player_coords[1]+background_block_y_center))
	elif direction == "east":
		for y in range (player_coords[1]-background_block_y_center-1, player_coords[1]+background_block_y_center+1):
			pos = str(player_coords[0]+background_block_x_center)+':'+str(y)
			if not pos in map.keys():
				GenerateWorld((player_coords[0]+background_block_x_center, y))
	elif direction == "west":
		for y in range (player_coords[1]-background_block_y_center-1, player_coords[1]+background_block_y_center+1):
			pos = str(player_coords[0]-background_block_x_center)+':'+str(y)
			if not pos in map.keys():
				GenerateWorld((player_coords[0]-background_block_x_center, y))

def GetElement(coords):
	global map
	pos = str(coords[0])+':'+str(coords[1])
	return map[pos]

def GenerateWorld(coords):
	global map
	map[str(coords[0])+':'+str(coords[1])]=random.randint(0,1)
