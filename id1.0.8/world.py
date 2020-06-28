
import random

def Init():
	global map
	map_size = map_size_x, map_size_y = 256, 256
	map=[]
	for x in range (map_size_x):
		row=[]
		for y in range (map_size_y):
			row.append(random.randint(0,1))
		map.append(row)
#	print(map[128][128])

def CalcChunk(player_coords):



def GetElement(coords):
	global map
	return map[coords[0]][coords[1]]
