import json
import os

SAVE_FILE = "savegame.json"


def save_game(player, scene):

    data = {
        "player_x": player.x,
        "player_y": player.y,
        "direction": player.direction,
        "scene": scene
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)


def load_game(player):

    if not os.path.exists(SAVE_FILE):
        return

    with open(SAVE_FILE, "r") as file:
        data = json.load(file)

    player.x = data["player_x"]
    player.y = data["player_y"]
    player.direction = data["direction"]

    player_rect = player.get_rect()
    player_rect.topleft = (player.x, player.y)

    return data.get("scene")