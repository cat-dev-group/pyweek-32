import arcade

from src.SCREAMING_SNAKE_SHOOTER import SnakeShooter


class StartScreen(arcade.View):
    """Create the greeting view screen."""

    def __init__(self, width, height):
        super().__init__()
        self.fill_color = arcade.make_transparent_color(
            arcade.color.BLACK, transparency=0
        )
        self.width = width
        self.height = height

    def on_draw(self):
        """Create displayed elements at the start."""
        arcade.draw_text(
            "Press Any Key to START",
            self.width / 2,
            self.height / 2,
            arcade.color.BRIGHT_GREEN,
            font_size=40,
            anchor_x="center",
            bold=True,
        )

    def on_key_press(self, symbol, modifiers):
        """Handle any key press to start."""
        # Don't start if print screen or windows key
        if symbol != 188978561024 and symbol != 65515:
            main_game = SnakeShooter()
            main_game.setup()
            self.window.show_view(main_game)
