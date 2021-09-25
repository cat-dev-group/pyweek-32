import os

import arcade
import arcade.gui
from dotenv import load_dotenv

from src.views.VendorView import VendorScreen

load_dotenv()
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT"))


class PauseScreen(arcade.View):
    """
    Create pause menu screen, with options to resume or quit.

    Will accept a passed scheduled function to "pause" with `arcade.unschedule`.
    """

    def __init__(
        self,
        game_view,
    ):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(
            arcade.color.WHITE, transparency=100
        )
        self.scheduled_function = game_view.add_enemy
        arcade.unschedule(self.scheduled_function)
        self.score = game_view.score
        self.guns = game_view.guns
        self.equipped_gun = game_view.equipped_gun
        self.all_sprites = game_view.all_sprites

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        vendor_button = arcade.gui.UIFlatButton(text="Go to Vendor Screen", width=200)
        self.v_box.add(vendor_button.with_space_around(bottom=20))

        # Handle Clicks
        @vendor_button.event("on_click")
        def on_click_flatbutton(event):

            vendor_view = VendorScreen(self)
            self.window.show_view(vendor_view)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box,
            )
        )

    def on_draw(self):
        """Create a pause menu with options to quit or resume."""
        self.game_view.on_draw()

        arcade.draw_lrtb_rectangle_filled(
            left=0,
            right=SCREEN_WIDTH,
            top=SCREEN_HEIGHT,
            bottom=0,
            color=self.fill_color,
        )

        current_score = f"Current score: {self.score:9}"
        arcade.draw_text(
            current_score,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 250,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press P to resume",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 200,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press ESC to quit",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 150,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )

        self.manager.draw()

    def on_key_press(self, symbol, modifiers):
        """Handle options to quit or resume."""
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.game_view.score = self.score
            self.game_view.equipped_gun = self.equipped_gun
            self.game_view.guns = self.guns
            try:
                self.all_sprites.append(self.equipped_gun)
                self.game_view.all_sprites = self.all_sprites
            except ValueError:
                pass
            self.game_view.equipped_gun.center_x = self.game_view.player.center_x
            self.game_view.on_draw()
            self.window.show_view(self.game_view)
            arcade.schedule(self.scheduled_function, 0.5)
