import pygame
from src.Game_Variables.game_variables import GameVariables as GV

def pause_screen(screen: pygame.Surface, save_message_timer, pause_bild):
    screen.blit(pause_bild, (0, 0))
    overlay = pygame.Surface((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    overlay.set_alpha(140)
    overlay.fill((0, 0, 0))
    pause_text = GV.FONT_BIG.render("PAUSIERT",True,(245, 230, 200))
    info_text = GV.FONT_SMALL.render("ESC = weiter | S = speichern | M = Menü | Q = Beenden",True,(230, 210, 180))
    screen.blit(overlay, (0, 0))
    screen.blit(pause_text,pause_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 - 40)))
    screen.blit(info_text,info_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 30)))
    if save_message_timer > 0:
        save_text = GV.FONT_SMALL.render("Erfolgreich gespeichert!",True,"light green")
        screen.blit(save_text,save_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 90)))
    pygame.display.flip()