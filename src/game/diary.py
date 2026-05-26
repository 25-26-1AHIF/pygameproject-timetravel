from src.Game_Variables.game_variables import GameVariables as GV
import pygame

class diary:
    def __init__(self, screen: pygame.Surface, filepath: str):
        self.screen = screen
        self.filepath = filepath

    def zeichnen(self):
        diary_bild = pygame.image.load(self.filepath).convert()
        #KI_Anfang;
        #benutzte KI: Microsoft Copilot
        # Prompt: Wie kann ich in Pycharm ein Sprite vergrößert darstellen,
        # ohne dass sich die Pixel des Bildes ändern? Geht das?
        # Muss ich dafür ein neues Sprite erstellen?
        scale_factor = 10  # z.B. 4x größer
        width = diary_bild.get_width() * scale_factor
        height = diary_bild.get_height() * scale_factor
        xpos_tagebuch = GV.SCREEN_WIDTH/2 - width/2
        ypos_tagebuch = GV.SCREEN_HEIGHT/2 - height/2
        sprite_big = pygame.transform.scale(diary_bild, (width, height))
        self.screen.blit(sprite_big, dest=(xpos_tagebuch, ypos_tagebuch))
        # KI-Ende
        titel_text_tagebuch = GV.FONT_MINI.render("Irgendwann im Mittelalter", True, "black")
        self.screen.blit(source=titel_text_tagebuch, dest=(xpos_tagebuch + 35, ypos_tagebuch + 60))
        medieval_icon = pygame.image.load("assets/Sprites/Icons/Medieval_Icon.png")
        height_bild = medieval_icon.get_height()/scale_factor
        width_bild = medieval_icon.get_width() / scale_factor
        icon_klein = pygame.transform.scale(medieval_icon, (width_bild, height_bild))
        self.screen.blit(source=icon_klein, dest=(xpos_tagebuch+50, ypos_tagebuch+100))
