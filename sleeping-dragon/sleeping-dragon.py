from pgzero.actor import *
from pgzero.screen import *
import math

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FONT_COLOUR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (200, 300)
ATTACK_DISTANCE = 200
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 3
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 100)),
    "eggs": Actor("one-egg", pos=(400, 100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 10,
    "sllep_counter": 0,
    "wake_counter": 0
}

medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 300)),
    "eggs": Actor("one-egg", pos=(400, 300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 7,
    "sllep_counter": 0,
    "wake_counter": 0
}

hard_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 500)),
    "eggs": Actor("one-egg", pos=(400, 500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 4,
    "sllep_counter": 0,
    "wake_counter": 0
}

lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor("hero", pos=HERO_START)

def draw():
    global lairs, eggs_collected, lives, game_complete
    Screen.clear()
    Screen.blit("dungeon", (0, 0))