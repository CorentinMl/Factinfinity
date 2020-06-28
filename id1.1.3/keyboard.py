import pygame
import player as Player
import display as Display
import __main__ as Main

def EventManager(event): #Event de pygame
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_F3:
			Display.ToggleDebugOverlay()
		if event.key == pygame.K_ESCAPE:
			Main.is_game_running = False
		if event.key == pygame.K_p:
			Main.is_game_paused = True
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			Player.ChangeDirection(event.key, "KEYDOWN")
	if event.type == pygame.KEYUP:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			Player.ChangeDirection(event.key, "KEYUP")
