#Initialisation des modules
import threading
import time
import random
from datetime import datetime
import sys
sys.path.append('../../lib')
import pygame

#Import des fichiers python du projet
import player as Player
import background as Background
import world as World

#Initialisation de pygame
pygame.init()

#Initialisations des variables
screen_size = screen_width, screen_height = 1500, 1000
screen_color = 255, 255, 255
is_game_running = True
is_game_paused = False
current_fps, past_fps, current_tps, past_tps = 0, 0, 0, 0

tick_per_second = 50
tick_sleep = 1/tick_per_second
tick_time_fix = 0.001

timing = pygame.time.Clock()

#Initialisation des modules:
Player.Init(screen_size)
World.Init()
Background.Init(screen_size)

#Initialisation de la fenêtre
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Jeu de test")

#Fonction de calcul des fps
def calc_perf():
	global past_fps, current_fps, past_tps, current_tps
	past_fps = current_fps
	past_tps = current_tps
	current_fps, current_tps = 0, 0
	if is_game_running:
		timer_fps = threading.Timer(1.0, calc_perf)
		timer_fps.start()

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

#Fonction d'affichage d'un texte à l'écran
def ShowMessage(texte, taille, police, couleur, x_coord, y_coord):
	TextPoliceInfo = pygame.font.SysFont(police, taille)
	TextMessage = TextPoliceInfo.render(texte, True, pygame.Color(couleur))
	TexteRectangle = TextMessage.get_rect()
	TexteRectangle.center = x_coord, y_coord
	screen.blit(TextMessage, TexteRectangle)
	#pygame.display.update()

#Fonction principale de calcul
def CalcTick():
	global current_tps
	#if not (y_ball+y_move <= 0 or y_ball+y_move >= fen_height-80):
	#	y_ball += y_move
	#if not (x_ball+x_move <= 0 or x_ball+x_move >= fen_width-80):
	#	x_ball += x_move

	#for i in range (number_balls):
	#	ball[i]=(ball[i][0]+x_move, ball[i][1]+y_move)

	current_tps+=1


def DoTick():
	global current_tps, tick_time_fix
	#if not game_over:
	#	timer_tick = threading.Timer(1, DoTick)
	#	timer_tick.start()
	#for i in range (tick_per_second):
	while is_game_running:
		next_tick = datetime.timestamp(datetime.now()) + tick_sleep
		CalcTick()
		#while datetime.timestamp(datetime.now()) < next_tick:
		#	timing.tick()
		time.sleep(next_tick-datetime.timestamp(datetime.now())-tick_time_fix)


calc_perf()
#DoTick()
timer_tick = threading.Timer(0.1, DoTick)
timer_tick.start()


#Boucle principale
while is_game_running:
	#On définit le fond de l'écran
	#screen.fill(screen_color)
	Background.Display(screen)
	Player.Display(screen)

	#Lecture des évènements d'entrée
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
		elif event.type == pygame.KEYDOWN:
			Player.EventManager(event)
			Background.EventManager(event)
			if event.key == pygame.K_p:
				ShowMessage("Jeu en pause", 100, "arial", "red", 500, 200)
				ShowMessage("Appuyez sur une touche pour continuer...", 20, "arial", "red", 500, 300)
				is_game_paused = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_move = 0
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				x_move = 0
		elif event.type == pygame.VIDEORESIZE:
			pygame.display.set_mode(event.size)


	#Affichage des éléments à l'écran
	#for i in range (number_balls):
	#	screen.blit(ball_image, (ball[i]))
	#screen.blit(ball_image, (x_ball,y_ball))
	ShowMessage(("Fps:"+str(past_fps)+" ,TPS:"+str(past_tps)), 20, "arial", "blue", 80, 20)
	pygame.display.flip()
	current_fps+=1
	if is_game_paused == True:
		while ResumeGame() == None:
			timing.tick()

pygame.quit()
quit()


#number_balls = 15
#ball = []
#for i in range (number_balls):
#	ball.append([random.randint(0, fen_width), random.randint(0, fen_height)]) #, random.randint(1, 10)
