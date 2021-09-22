import arcade

from .SCREAMING_SNAKE_SHOOTER import SnakeShooter

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SCREAMING_SNAKE_SHOOTER"

if __name__ == "__main__":
    screaming_snake_shooter = SnakeShooter(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )
    screaming_snake_shooter.setup()
    arcade.run()
