import random
import math
import sqlite3
import database as Database
import player as Player
import background as Background

ENTITY_TYPE_PLAYER = 1

BACKGROUND_TYPE_ERROR = 0
BACKGROUND_TYPE_DIRT = 1
BACKGROUND_TYPE_GRASS = 2

def Init():
	global map, obj_seed
	map={}
	obj_seed = Database.LoadWorldSeed()
	if not obj_seed:
		obj_seed = GenerateSeed()
	LoadWorldAroundPostition(Player.GetAbsoluteCoords())
	Database.Commit()

#	print(map[128][128])

def LoadWorldAroundPostition(coords, radius = 100):
	for x in range (coords[0]-radius, coords[0]+radius):
		for y in range (coords[1]-radius, coords[1]+radius):
			LoadWorld((x,y))


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
				LoadWorld((x, player_coords[1]-background_block_y_center-1))
	elif direction == "south":
		for x in range (player_coords[0]-background_block_x_center-2, player_coords[0]+background_block_x_center+2):
			pos = str(x)+':'+str(player_coords[1]+background_block_y_center+1)
			if not pos in map.keys():
				LoadWorld((x, player_coords[1]+background_block_y_center+1))
			#print(pos)
	elif direction == "east":
		for y in range (player_coords[1]-background_block_y_center-2, player_coords[1]+background_block_y_center+2):
			pos = str(player_coords[0]+background_block_x_center+1)+':'+str(y)
			if not pos in map.keys():
				LoadWorld((player_coords[0]+background_block_x_center+1, y))
	elif direction == "west":
		for y in range (player_coords[1]-background_block_y_center-2, player_coords[1]+background_block_y_center+2):
			pos = str(player_coords[0]-background_block_x_center-1)+':'+str(y)
			if not pos in map.keys():
				LoadWorld((player_coords[0]-background_block_x_center-1, y))

def GetElement(coords):
	global map
	pos = str(coords[0])+':'+str(coords[1])
	if not pos in map.keys():
		#print("Erreur à la position:", pos)
		return 0
	else:
		return map[pos]

def LoadWorld(coords):
	element = Database.GetElement(coords)
	if element != None:
		map[str(coords[0])+':'+str(coords[1])] = element
	else:
		GenerateWorld(coords)

def DeleteWorld():
	global map, rando1, rando2
	Database.DeleteWorldData()
	Init()
	Background.CalcPositions()

def GenerateSeed(type = "sinusoid"):
	obj_seed = {
		"type" : "sinusoid",
		"number" : random.randint(1, 4),
		"random" : []
	}

	if type == "sinusoid":
		for loop in range (obj_seed["number"]):
			obj_seed["random"].append(0.5+random.random()*random.randint(3, 20))
		Database.SaveWorldSeed(obj_seed)
		return obj_seed


def GenerateWorld(coords):
	global map
	distance_init = math.sqrt((coords[0])**2+(coords[1])**2)
	distance = 0
	for loop in range (obj_seed["number"]):
		distance += math.cos(obj_seed["random"][loop]*distance_init)

	if distance >= 0:
		element = 1
	else:
		element = 2

#	element = random.randint(0,1)
	map[str(coords[0])+':'+str(coords[1])] = element
	Database.AddElementToMap((coords[0], coords[1], element))
