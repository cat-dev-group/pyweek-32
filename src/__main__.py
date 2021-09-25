import os

import arcade
from dotenv import load_dotenv

from src.views.StartView import StartScreen

load_dotenv()
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT"))

SCREEN_TITLE = "SCREAMING_SNAKE_SHOOTER"

if __name__ == "__main__":
    window = arcade.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
    start = StartScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.show_view(start)
    arcade.run()
