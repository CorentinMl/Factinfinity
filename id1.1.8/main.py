#Initialisation des modules
import threading
import time
import random
from datetime import datetime
import sys

sys.path.append('../../lib')
import pygame

sys.path.append('.')
#Import des fichiers python du projet
import player as Player
import background as Background
import world as World
import keyboard as Keyboard
import display as Display
import database as Database
import command as Command

#Initialisation de pygame
pygame.init()

#FPS
screen_size = screen_width, screen_height = 1500, 1000
screen_color = 255, 255, 255

#TPS
time_tick = 0
tick_per_second = 30
tick_sleep = 1/tick_per_second
tick_time_fix = 0.001
current_fps, past_fps, current_tps, past_tps, average_fps_time = 0, 0, 0, 0, 0
is_game_running = True
is_game_paused = False
is_tps_init_finished = False
timing = pygame.time.Clock()

event_list = []

#Initialisation de la fenêtre
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Jeu de test")

#Fonction de calcul des fps
def calc_perf():
	global past_fps, current_fps, past_tps, current_tps, average_fps_time
	while is_game_running:
		past_fps = current_fps
		past_tps = current_tps
		if past_fps !=0:
			average_fps_time = 1/past_fps
		current_fps, current_tps = 0, 0
		time.sleep(1)

#Fonction de pause du jeu
def ResumeGame():
	global is_game_paused, is_game_running
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
		if event.type == pygame.QUIT:
			is_game_running = False
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			is_game_paused = False
			return event.key
	return None

def Tps():
	global current_tps, tick_time_fix, time_tick, is_tps_init_finished
	Database.Init()
	Player.CalcInit()
	World.Init()
	Command.Init()
	is_tps_init_finished = True
	next_tick = datetime.timestamp(datetime.now()) + tick_sleep
	while is_game_running:
		time_now = datetime.timestamp(datetime.now())
		CalcTick()
		time_tick = datetime.timestamp(datetime.now()) - time_now
		time_wait = next_tick-datetime.timestamp(datetime.now())-tick_time_fix
		if time_wait > 0:
			time.sleep(time_wait)
		next_tick = datetime.timestamp(datetime.now()) + tick_sleep
		current_tps+=1
	Database.Close()

def Fps():
	global current_fps
	#Initialisation des modules:
	while is_tps_init_finished == False:
		time.sleep(0.01)
	Player.DisplayInit(screen_size)
	Background.Init(screen_size)
	World.PostInit(Background.GetBackgroundBlockNumber())
	Display.Init()
	while is_game_running:
		if Player.is_player_moving:
			Background.CalcPositions()
		Background.Display(screen)
		Player.Display(screen)
		Display.Display(screen, screen_size)
		pygame.display.flip()
		current_fps+=1
		if is_game_paused == True:
			while ResumeGame() == None:
				timing.tick()

#Fonction principale de calcul
def CalcTick():
	Keyboard.EventManager()
	Player.Move()

thread_tps = threading.Thread(target=Tps)
thread_fps = threading.Thread(target=Fps)
thread_perf = threading.Thread(target=calc_perf)
thread_perf.start()
thread_tps.start()
thread_fps.start()


#Boucle principale
while is_game_running:
	#Lecture des évènements d'entrée
	time.sleep(0.1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			event_list.append(event)
			#Keyboard.EventManager(event)
		elif event.type == pygame.VIDEORESIZE:
			pygame.display.set_mode(event.size)

pygame.quit()
