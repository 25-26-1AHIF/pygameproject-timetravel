import json
import os
import pygame
from src.Game_Variables.game_variables import GameVariables as GV

SAVE_FILE = "savegame.json"


def save_game(player, scene):
    if GV.STARTED_TIME:
        elapsed = pygame.time.get_ticks() - GV.START_TIME - GV.PAUSED_TIME
    else:
        elapsed = 0

    data = {
        "player_x": player.x,
        "player_y": player.y,
        "direction": player.direction,
        "scene": scene,

        "started_time": GV.STARTED_TIME,
        "elapsed": elapsed,

        "candle": GV.CANDLE_IN_INVENTORY,
        "shield": GV.SHIELD_IN_INVENTORY,
        "crown": GV.CROWN_IN_INVENTORY,
        "got_all": GV.GOT_ALL_ITEMS,
        "inventory": GV.PLAYER_INVENTORY["inventory"],
        "found_candle": GV.FOUND_CANDLE_BUTTON_PRESSED,
        "found_shield": GV.FOUND_SHIELD_BUTTON_PRESSED,
        "found_crown": GV.FOUND_CROWN_BUTTON_PRESSED,
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)


def load_game(player):
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as file:
        data = json.load(file)

    player.x = data["player_x"]
    player.y = data["player_y"]
    player.direction = data["direction"]

    player_rect = player.get_rect()
    player_rect.topleft = (player.x, player.y)

    GV.STARTED_TIME = data.get("started_time", False)
    if GV.STARTED_TIME:
        GV.START_TIME = pygame.time.get_ticks() - data.get("elapsed", 0)
        GV.PAUSED_TIME = 0

    GV.CANDLE_IN_INVENTORY = data.get("candle", False)
    GV.SHIELD_IN_INVENTORY = data.get("shield", False)
    GV.CROWN_IN_INVENTORY = data.get("crown", False)
    GV.GOT_ALL_ITEMS = data.get("got_all", False)
    GV.PLAYER_INVENTORY["inventory"] = data.get("inventory", [])
    GV.FOUND_CANDLE_BUTTON_PRESSED = data.get("found_candle", False)
    GV.FOUND_SHIELD_BUTTON_PRESSED = data.get("found_shield", False)
    GV.FOUND_CROWN_BUTTON_PRESSED = data.get("found_crown", False)

    return data.get("scene")