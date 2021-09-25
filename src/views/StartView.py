import arcade

from src.SCREAMING_SNAKE_SHOOTER import SnakeShooter
from pathlib import Path


class StartScreen(arcade.View):
    """Create the greeting view screen."""

    def __init__(self, width, height):
        super().__init__()
        self.fill_color = arcade.make_transparent_color(
            arcade.color.BLACK, transparency=0
        )
        self.width = width
        self.height = height

        # plays start jingle
        sound_src = Path.cwd() / "src" / "sounds" / "test_jingle.wav"
        self.jingle_sound_object = arcade.load_sound(sound_src)
        self.mus_player = arcade.play_sound(self.jingle_sound_object, volume=0.5)

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

            # stop sound if user starts game prematurely
            if self.jingle_sound_object.is_playing(self.mus_player):
                arcade.stop_sound(self.mus_player)

            main_game = SnakeShooter()
            main_game.setup()
            self.window.show_view(main_game)
