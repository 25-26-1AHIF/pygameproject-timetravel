import pygame
import json
from src.Game_Variables.game_variables import GameVariables as GV, GameScreens

# KI-Anfang:
# benutzte KI: Microsoft Copilot
# URL: https://copilot.microsoft.com
# Prompt: Wie kann ich nochmal eine Player Eingabe auf dem Screen machen?
# Bemerkung: Ein großteil des Codes ist von Copilot generiert hier im leaderboard, jedoch habe ich es selber debuggt
# Zum Beispiel gab es einen Zähl-Error den ich ohne KI gefixed habe und auch in eine Klasse habe ich es umgewandelt,
# nicht die KI.

class Leaderboard():

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        self.LEADERBOARD_FILE = "Game_Variables/leaderboard.json"
        self.screen = screen
        self.clock = clock
        self.background = pygame.image.load("assets/Bilder/Hintergrundbild für Leaderboard.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    def save_score(self, name, time):
        try:
            with open(self.LEADERBOARD_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({"name": name, "time": time})
        data = sorted(data, key=lambda x: x["time"])  # schnellste zuerst

        with open(self.LEADERBOARD_FILE, "w") as f:
            json.dump(data, f, indent=4)


    def load_scores(self):
        try:
            with open(self.LEADERBOARD_FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def print_leaderboard(self):
        font = pygame.font.SysFont("Georgia", 32)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameScreens.MAIN

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return GameScreens.MAIN

            self.screen.fill("black")
            self.screen.blit(self.background, (0,0))

            scores = self.load_scores()

            title = font.render("Leaderboard", True, (255, 255, 0))
            self.screen.blit(title, (450, 100))

            y = 160
            for entry in scores[:10]:
                line = f"{entry['name']} - {entry['time']:.2f} Sekunden"
                surf = font.render(line, True, ("black"))
                self.screen.blit(surf, (350, y))
                y += 40

            exit_text = font.render("Drücke ESC um zurückzukehren", True, ("black"))
            self.screen.blit(exit_text, (350, y + 40))

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def leaderboard(self, final_time):
        GV.init()

        font = pygame.font.SysFont("Georgia", 32)

        player_name = ""
        entering_name = True

        frame_x = 400
        frame_y = 250
        frame_w = 400
        frame_h = 50

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if entering_name:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            entering_name = False
                            self.save_score(player_name, final_time)

                        elif event.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]

                        else:
                            player_name += event.unicode

                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return GameScreens.MAIN

            self.screen.fill("black")
            self.screen.blit(self.background, (0,0))

            if entering_name:
                pygame.draw.rect(self.screen, ("black"), (frame_x, frame_y, frame_w, frame_h), 2)
                text_surface = font.render(player_name, True, ("black"))
                self.screen.blit(text_surface, (frame_x + 10, frame_y + 10))

                info = font.render("Gib deinen Namen ein und drücke ENTER", True, ("black"))
                self.screen.blit(info, (frame_x - 150, frame_y - 50))

            else:
                scores = self.load_scores()

                title = font.render("Leaderboard", True, (255, 255, 0))
                self.screen.blit(title, (frame_x + 50, 100))

                y = 160
                for entry in scores[:10]:
                    line = f"{entry['name']} - {entry['time']:.2f} Sekunden"
                    surf = font.render(line, True, ("black"))
                    self.screen.blit(surf, (frame_x - 50, y))
                    y += 40

                exit_text = font.render("Drücke ESC um zurückzukehren", True, ("black"))
                self.screen.blit(exit_text, (frame_x - 50, y + 40))

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
# KI-Ende
# Bemerkung: Weil der Code fragmente von KI-Code und fragmenten meines Codes beeinhaltet,
# habe ich das KI-Ende hier unten hingeschrieben, damit es nicht zu kompliziert wird
# NICHT REIN KI GENERIERTER CODE!!