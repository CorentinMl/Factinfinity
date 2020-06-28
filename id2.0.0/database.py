import sqlite3
import player as Player
import json

def Init():
	global database_loc, database_connection
	database_loc = "../../sav/save.bd"
	database_connection = sqlite3.connect(database_loc)
	database_cursor = database_connection.cursor()
	database_cursor.execute("CREATE TABLE IF NOT EXISTS Map (coord_x integer, coord_y integer, element integer, PRIMARY KEY (coord_x, coord_y))")
	database_cursor.execute("CREATE TABLE IF NOT EXISTS Entity (type integer, name VARCHAR(50), coord_x float, coord_y float, direction integer, speed float, PRIMARY KEY (type, name))")
	database_cursor.execute("CREATE TABLE IF NOT EXISTS Generaldata (name VARCHAR(50), value TEXT, PRIMARY KEY (name))")
	database_connection.commit()
	database_cursor.close()
	#database_connection.close()

def Close():
	SaveGame()
	#database_cursor.close()
	database_connection.close()

def AddElementToMap(values):
	database_cursor = database_connection.cursor()
	database_cursor.execute("INSERT INTO Map (coord_x, coord_y, element) VALUES (?, ?, ?)", values)
	database_cursor.close()

def GetElement(coords):
	database_cursor = database_connection.cursor()
	result = None
	for row in database_cursor.execute("SELECT element FROM Map WHERE coord_x=? AND coord_y=?", coords):
		result = row[0]
	database_cursor.close()
	return(result)

def DeleteWorldData():
	database_cursor = database_connection.cursor()
	database_cursor.execute("DELETE FROM Map")
	database_cursor.execute("DELETE FROM Generaldata WHERE name = 'world_seed'")
	database_connection.commit()
	database_cursor.close()

def SaveGame():
	database_cursor = database_connection.cursor()
	database_cursor.execute("INSERT OR REPLACE INTO Entity (type, name, coord_x, coord_y, direction, speed) VALUES (1, 'Player', ?, ?, ?, ?)", Player.GetData())
	database_cursor.close()
	Commit()

def Commit():
	try:
		#database_connection = sqlite3.connect(database_loc)
		#database_cursor = database_connection.cursor()
		#database_cursor.execute(request, values)
		database_connection.commit()
		#database_cursor.close()
		#database_connection.close()
	except sqlite3.Error as error:
		print("SQLite 3 Error:", error)


def LoadPlayer():
	database_cursor = database_connection.cursor()
	data = None
	for row in database_cursor.execute("SELECT * FROM Entity WHERE type=1 LIMIT 1"):
		data = row
	database_cursor.close()
	return data

def SaveWorldSeed(seed):
	database_cursor = database_connection.cursor()
	json_seed = json.dumps(seed)
	database_cursor.execute("INSERT OR REPLACE INTO Generaldata (name, value) VALUES ('world_seed',?)", [json_seed])
	database_cursor.close()

def LoadWorldSeed():
	database_cursor = database_connection.cursor()
	seed = None
	for row in database_cursor.execute("SELECT value FROM Generaldata WHERE name='world_seed' LIMIT 1"):
		seed = json.loads(row[0])
	database_cursor.close()
	return seed
