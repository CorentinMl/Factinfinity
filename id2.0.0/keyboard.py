import pygame
import player as Player
import display as Display
import __main__ as Main
import command as Command

def EventManager(): #Event de pygame
	if len(Main.event_list) > 0:
		event = Main.event_list.pop(0)
		ExecuteEvent(event)


def ExecuteEvent(event):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_F3:
			Display.ToggleDebugOverlay()
		if Command.is_chat_open:
			if event.key == pygame.K_UP:
				Command.Autocomplete("previous")
			elif event.key == pygame.K_DOWN:
				Command.Autocomplete("next")
			else:
				Command.ModifyCommand(event)
		else:
			if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
				Player.ChangeDirection(event.key, "KEYDOWN")
			elif event.key == pygame.K_ESCAPE:
				Main.is_game_running = False
			elif event.key == pygame.K_p:
				Main.is_game_paused = True
			elif event.key == pygame.K_t:
				Command.OpenChat()
			elif event.key == pygame.K_KP_DIVIDE:
				Command.OpenChat(True)
	if event.type == pygame.KEYUP:
		if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT):
			Player.ChangeDirection(event.key, "KEYUP")
