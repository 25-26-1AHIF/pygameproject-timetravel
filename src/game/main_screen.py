import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens

def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Main")
    title_font = pygame.font.SysFont("Georgia",82,bold=True)
    subtitle_font = pygame.font.SysFont("Georgia",28)
    button_font = pygame.font.SysFont("Georgia",38)
    title_text = title_font.render("TimeTravel",True,(245, 230, 200))
    subtitle_text = subtitle_font.render("Was für ein Geheimnis kann ein Tagebuch beherbergen?",True,(235, 220, 190))
    new_game_text = button_font.render("Neues Spiel",True,(255, 240, 210))
    load_text = button_font.render("Spielstand laden",True,(255, 240, 210))
    quit_text = button_font.render("Beenden",True,(255, 240, 210))
    title_rect = title_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 120))
    subtitle_rect = subtitle_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 180))
    new_game_rect = new_game_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 380))
    load_rect = load_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 445))
    quit_rect = quit_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 510))
    Main_screen_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    Main_screen_bild = pygame.transform.scale(Main_screen_bild,(GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                elif load_rect.collidepoint(event.pos):
                    return GameScreens.LADEN
                elif quit_rect.collidepoint(event.pos):
                    return None
        screen.blit(Main_screen_bild, (0, 0))
        shadow_title = title_font.render("TimeTravel",True,(40, 20, 10))

        screen.blit(shadow_title,title_rect.move(4, 4))

        screen.blit(title_text, title_rect)
        screen.blit(subtitle_text, subtitle_rect)

        buttons = [
            ("Neues Spiel", new_game_rect),
            ("Spielstand laden", load_rect),
            ("Beenden", quit_rect)]
        for text, rect in buttons:
            hover = rect.collidepoint(mouse_pos)
            color = (
                (255, 240, 210)
                if hover else
                (220, 195, 160))
            label = button_font.render(text, True,color)
            label_rect = label.get_rect(center=rect.center)
            screen.blit(label, label_rect)
            if hover:
                pygame.draw.line(
                    screen,
                    color,
                    (label_rect.left, label_rect.bottom + 5),
                    (label_rect.right, label_rect.bottom + 5),
                    2)
        pygame.display.flip()
        clock.tick(60)
