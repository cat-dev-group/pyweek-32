import arcade
from dotenv import load_dotenv

from .SCREAMING_SNAKE_SHOOTER import StartView

load_dotenv("./.env")
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "SCREAMING_SNAKE_SHOOTER"

if __name__ == "__main__":
    window = arcade.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
    start = StartView()
    window.show_view(start)
    arcade.run()
