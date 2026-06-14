from src.Game_Variables.game_variables import GameVariables as GV
import pygame

class diary:
    def __init__(self, screen: pygame.Surface, filepath: str):
        self.screen = screen
        self.filepath = filepath
        self.diary_bild = pygame.image.load(self.filepath).convert_alpha()
        self.font_mini = pygame.font.SysFont("Georgia",10)
        self.scale_factor = 10  # z.B. 4x größer
        self.width = self.diary_bild.get_width() * self.scale_factor
        self.height = self.diary_bild.get_height() * self.scale_factor
        self.xpos_tagebuch = GV.SCREEN_WIDTH/2 - self.width/2
        self.ypos_tagebuch = GV.SCREEN_HEIGHT/2 - self.height/2
        self.medievel_icon_pos = (self.xpos_tagebuch+50, self.ypos_tagebuch+100)
        medieval_icon = pygame.image.load("assets/Sprites/Icons/Medieval_Icon.png")
        height_bild = medieval_icon.get_height() / self.scale_factor
        width_bild = medieval_icon.get_width() / self.scale_factor
        self.icon_klein = pygame.transform.scale(medieval_icon, (width_bild, height_bild))

    def draw(self):
        #KI_Anfang;
        #benutzte KI: Microsoft Copilot
        # Prompt: Wie kann ich in Pycharm ein Sprite vergrößert darstellen,
        # ohne dass sich die Pixel des Bildes ändern? Geht das?
        # Muss ich dafür ein neues Sprite erstellen?
        sprite_big = pygame.transform.scale(self.diary_bild, (self.width, self.height))
        self.screen.blit(sprite_big, dest=(self.xpos_tagebuch, self.ypos_tagebuch))
        # KI-Ende
        titel_text_tagebuch = self.font_mini.render("Irgendwann im Mittelalter", True, "black")
        self.screen.blit(source=titel_text_tagebuch, dest=(self.xpos_tagebuch + 35,self.ypos_tagebuch + 60))
        self.screen.blit(source=self.icon_klein, dest=(self.xpos_tagebuch+50, self.ypos_tagebuch+100))
