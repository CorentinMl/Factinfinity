import player as Player
import __main__ as Main
import pygame
import command as Command
import world as World


def Init():
	global debug_menu_state
	debug_menu_state = False

#Fonction d'affichage d'un texte à l'écran
def ShowMessage(screen, texte, taille, police, couleur, x_coord, y_coord, center = False):
	TextPoliceInfo = pygame.font.SysFont(police, taille)
	TextMessage = TextPoliceInfo.render(texte, True, pygame.Color(couleur))
	TexteRectangle = TextMessage.get_rect()
	if center:
		TexteRectangle.center = x_coord, y_coord
	else:
		TexteRectangle = x_coord, y_coord
	screen.blit(TextMessage, TexteRectangle)


def Display(screen, screen_size):
	if debug_menu_state:
		ShowMessage(screen, ("Fps:"+str(Main.past_fps)+" (average time = {0:.2f}".format(Main.average_fps_time*1000)+" ms) ,TPS:"+str(Main.past_tps)), 20, "arial", "yellow", 10, 10)
		ShowMessage(screen, ("Tick time:"+str(Main.time_tick)), 20, "arial", "yellow", 10, 30)
		ShowMessage(screen, ("x = {0:.2f}".format(Player.player_x_coord)+" ,y = {0:.2f}".format(Player.player_y_coord)), 20, "arial", "yellow", 10, 50)
		ShowMessage(screen, ("direction = "+str(Player.player_move_direction)), 20, "arial", "yellow", 10, 70)
		ShowMessage(screen, ("speed = "+str(Player.player_speed)), 20, "arial", "yellow", 10, 90)
		ShowMessage(screen, ("is moving = "+str(Player.is_player_moving)), 20, "arial", "yellow", 10, 110)
		ShowMessage(screen, ("is chat open = "+str(Command.is_chat_open)), 20, "arial", "yellow", 10, 130)
		ShowMessage(screen, ("seed_type = "+str(World.obj_seed["type"])), 20, "arial", "yellow", 10, 150)
		ShowMessage(screen, ("seed_number = "+str(World.obj_seed["number"])), 20, "arial", "yellow", 10, 170)
		ShowMessage(screen, ("seed_random = "+str(World.obj_seed["random"])), 20, "arial", "yellow", 10, 190)
	if Main.is_game_paused:
		ShowMessage(screen, "Jeu en pause", 100, "arial", "red", 500, 200)
		ShowMessage(screen, "Appuyez sur une touche pour continuer...", 20, "arial", "red", 500, 300)
	if Command.is_chat_open:
		ShowMessage(screen, (Command.chat_command+"_"), 30, "arial", "red", 10, screen_size[1]-40)
#	chat_len = len(Command.chat_history)
#	for loop in range (chat_len):
#		ShowMessage(screen, (Command.chat_history[chat_len-loop][0]), 20, "arial", Command.chat_history[chat_len-loop][1], 10, screen_size[1]-60-20*(chat_len-loop))
	index = 0
	for value in reversed(Command.chat_history):
		ShowMessage(screen, (value[0]), 20, "arial", value[1], 10, screen_size[1]-60-20*index)
		index += 1


def ToggleDebugOverlay():
	global debug_menu_state
	debug_menu_state = not debug_menu_state
