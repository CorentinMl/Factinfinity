import pygame
import player as Player
import database as Database
import __main__ as Main
import world as World
import background as Background

def Init():
	global is_chat_open, chat_command, number_history, chat_history, command_history
	number_history = 10
	#chat_history = [("", "", "yellow")] * number_history
	chat_history = []
	command_history = []
	is_chat_open = False
	chat_command = ""


def OpenChat(command = False):
	global is_chat_open, chat_command, autocomplete
	is_chat_open = True
	autocomplete = -1
	if command:
		chat_command = "/"

def Autocomplete(action):
	global autocomplete, chat_command
	index_max = len(command_history)-1
	if index_max >= 0:
		if action == "previous":
			if autocomplete < index_max:
				autocomplete +=1
		elif action == "next":
			if autocomplete == 0:
				autocomplete = -1
			elif autocomplete >= 1:
				autocomplete -=1
		if autocomplete == -1:
			chat_command = ""
		else:
			chat_command = command_history[autocomplete]

def ModifyCommand(event):
	global is_chat_open, chat_command, autocomplete
	if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
		if len(chat_command) > 0:
			SendCommand(chat_command)
		chat_command = ""
		is_chat_open = False
	elif event.key == pygame.K_ESCAPE:
		chat_command = ""
		is_chat_open = False
	elif event.key == pygame.K_BACKSPACE:
		chat_command = chat_command[:-1]
		autocomplete = -1
	else:
		chat_command += event.unicode

def AddToChat(text, color = "yellow"):
	chat_history.append((text, color))
	if len(chat_history) > number_history:
		chat_history.pop(0)
#	for index in range (number_history):
#		number = number_history-index-1
#		if number == 0:
#			chat_history[0] = (text, command, color)
#		else:
#			chat_history[number] = chat_history[number-1]

def SendCommand(command):
	global command_history
	command_history.insert(0, command)
	if command[0] == "/":
		command = command.split(" ")
		long = len(command)
		if command[0] == "/speed":
			if long < 2:
				AddToChat("[Console] Info: Syntaxe: '/speed <number>' Description: Change la vitesse du joueur (bloc par tick).", "orange")
			else:
				try:
					speed = float(command[1])
				except ValueError:
					AddToChat("[Console] Erreur: Nombre '"+str(command[1])+"' invalide!", "red")
				else:
					Player.player_speed = speed
					AddToChat("[Console] Succès: Nouvelle vitesse du joueur: "+str(speed), "green")
		elif command[0] == "/tps":
			if long < 2:
				AddToChat("[Console] Info: Syntaxe: '/tps <integer>' Description: Change le nombre de TPS (tick per second).", "orange")
			else:
				try:
					value = int(command[1])
				except ValueError:
					AddToChat("[Console] Erreur: Nombre '"+str(command[1])+"' invalide (pas un entier)! Nombre entier positif attendu.", "red")
				else:
					if value <0:
						AddToChat("[Console] Erreur: Nombre '"+str(command[1])+"' invalide (nombre négatif)! Nombre entier positif attendu.", "red")
					else:
						Main.tick_per_second = value
						Main.tick_sleep = 1/value
						AddToChat("[Console] Succès: Nouvelle vitesse du nombre de TPS: "+str(value), "green")
		elif command[0] == "/tp":
			if long < 3:
				AddToChat("[Console] Info: Syntaxe: '/tp <x coords> <y coords>' Description: Télporte du joueur.", "orange")
			else:
				try:
					x = float(command[1])
					y = float(command[2])
				except ValueError:
					AddToChat("[Console] Erreur: Coordonnées invalides!", "red")
				else:
					Player.Teleport(x, y)
					AddToChat("[Console] Succès: Joueur téléporté en: x = "+str(x)+", y = "+str(y), "green")
		elif command[0] == "/save":
			Database.SaveGame()
			AddToChat("[Console] Succès: Monde sauvegardé", "green")
		elif command[0] == "/close":
			Main.is_game_running = False
			AddToChat("[Console] Succès: Arrêt du jeu...", "green")
		elif command[0] == "/refresh":
			AddToChat("[Console] Rechargement de la zone...", "purple")
			World.LoadWorldAroundPostition(Player.GetAbsoluteCoords(), 50)
			Background.CalcPositions()
			AddToChat("[Console] Succès: Zone rechargée!", "green")
		elif command[0] == "/resetmap":
			if long < 2:
				AddToChat("[Console] Info: Etes-vous sûr de vouloir détruire la sauvegarde? Tapez '/resetmap confirm' pour confirmer.", "orange")
			else:
				if command[1] == "confirm":
					World.DeleteWorld()
					AddToChat("[Console] Succès: Sauvegarde supprimée, génération du nouveau monde...", "green")
				else:
					AddToChat("[Console] Info: Syntaxe: '/resetmap confirm' Description: Supprime définitivement la sauvegarde.", "orange")
		elif command[0] == "/printload":
			print(World.map)
			AddToChat("[Console] Succès: Coordonnées des emplacements chargés envoyés dans la console.", "green")
		else:
			AddToChat("[Console] Erreur: Commande Inconnue!", "red")
	else:
		AddToChat(command)
