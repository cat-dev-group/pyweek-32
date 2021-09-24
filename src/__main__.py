import arcade

from src.views.StartView import StartScreen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "SCREAMING_SNAKE_SHOOTER"

if __name__ == "__main__":
    window = arcade.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
    start = StartScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.show_view(start)
    arcade.run()
