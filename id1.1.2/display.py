import player as Player
import __main__ as Main
import pygame


def Init():
	global debug_menu_state
	debug_menu_state = 0

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


def Display(screen):
	if debug_menu_state:
		ShowMessage(screen, ("Fps:"+str(Main.past_fps)+" ,TPS:"+str(Main.past_tps)+" ,time tick:"+str(Main.time_tick)), 20, "arial", "yellow", 10, 10)
		ShowMessage(screen, ("x= {0:.2f}".format(Player.player_x_coord)+" ,y= {0:.2f}".format(Player.player_y_coord)), 20, "arial", "yellow", 10, 30)
		ShowMessage(screen, ("dir="+str(Player.player_move_direction)), 20, "arial", "yellow", 10, 50)
		ShowMessage(screen, ("is_move="+str(Player.is_player_moving)), 20, "arial", "yellow", 10, 70)
	if Main.is_game_paused:
		ShowMessage(screen, "Jeu en pause", 100, "arial", "red", 500, 200)
		ShowMessage(screen, "Appuyez sur une touche pour continuer...", 20, "arial", "red", 500, 300)


def ToggleDebugOverlay():
	global debug_menu_state
	debug_menu_state = 1-debug_menu_state
