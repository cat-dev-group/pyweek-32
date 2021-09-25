import os

import arcade
from dotenv import load_dotenv

load_dotenv()
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT"))


class VendorScreen(arcade.View):
    """Create the vendor screen."""

    def __init__(
        self,
        pause_view,
        score,
    ):
        super().__init__()
        self.pause_view = pause_view
        self.score = score

    def on_draw(self):
        """Create displayed elements at the start."""
        self.pause_view.on_draw()

        arcade.draw_lrtb_rectangle_filled(
            left=0,
            right=SCREEN_WIDTH,
            top=SCREEN_HEIGHT,
            bottom=0,
            color=arcade.color.BLACK,
        )

        vendor_text = f"Your current score is: {self.score:9}"

        arcade.draw_text(
            "Welcome to the Vendor!",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 100,
            arcade.color.ORANGE,
            font_size=40,
            anchor_x="center",
            bold=True,
        )
        arcade.draw_text(
            vendor_text,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 150,
            arcade.color.ORANGE,
            font_size=30,
            anchor_x="center",
            bold=True,
        )
        arcade.draw_text(
            "Press P to resume",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 200,
            arcade.color.ORANGE,
            font_size=20,
            anchor_x="center",
        )

    def on_key_press(self, symbol, modifiers):
        """Handle any key press to start."""
        # Don't start if print screen or windows key
        if symbol == arcade.key.P:
            self.window.show_view(self.pause_view)
