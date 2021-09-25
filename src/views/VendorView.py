import os
import pathlib

import arcade
import arcade.gui
from dotenv import load_dotenv

from src.base_classes.gun import Gun
from src.error_throwing import ErrorType

load_dotenv()
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT"))


class VendorScreen(arcade.View):
    """Create the vendor screen."""

    def __init__(
        self,
        pause_view,
    ):
        super().__init__()
        self.pause_view = pause_view
        self.score = pause_view.score
        self.equipped_gun = pause_view.equipped_gun
        self.selected_text = ""
        self.selected_gun = self.equipped_gun
        self.all_sprites = pause_view.all_sprites

        # start gui manager to handle buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # code for adding clickable buttons for guns
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        # create guns
        PY90 = Gun(
            gun_name="PY90",
            ammo=10000,
            rof=20,
            mag_size=10000,
            specialty=ErrorType.PYTHON,
            price=500,
            image=pathlib.Path("src/images/KRISS.png"),
            scale=0.5,
            angle=90,
        )
        STDLIB47 = Gun(
            gun_name="STDLIB47",
            ammo=10000,
            rof=20,
            mag_size=10000,
            specialty=ErrorType.PYTHON,
            price=10000,
            image=pathlib.Path("src/images/BAIKAL.png"),
            scale=0.5,
            angle=90,
        )
        EX47 = Gun(
            gun_name="EX47",
            ammo=10000,
            rof=20,
            mag_size=10000,
            specialty=ErrorType.PYTHON,
            price=1000000,
            image=pathlib.Path("src/images/AK47.png"),
            scale=0.5,
            angle=90,
        )

        available_guns = {
            "PY90": PY90,
            "STDLIB47": STDLIB47,
            "EX47": EX47,
        }

        # create gun text
        gun1_text = "PY90"
        gun2_text = "STDLIB47"
        gun3_text = "EX47"

        # create gun buttons
        gun1 = arcade.gui.UIFlatButton(text=gun1_text, width=230)
        gun2 = arcade.gui.UIFlatButton(text=gun2_text, width=230)
        gun3 = arcade.gui.UIFlatButton(text=gun3_text, width=230)

        # add buttons
        self.h_box.add(gun1.with_space_around(top=5, right=5, bottom=5, left=5))
        self.h_box.add(gun2.with_space_around(top=5, right=5, bottom=5, left=5))
        self.h_box.add(gun3.with_space_around(top=5, right=5, bottom=5, left=5))

        # handle clicking on buttons
        @gun1.event("on_click")
        @gun2.event("on_click")
        @gun3.event("on_click")
        def on_click_gun(event):
            self.selected_text = event.source.text

        # setup code for clickable `git push` button
        git_style = {
            "font_size": 15,
            "font_color": arcade.color.CHARTREUSE,
            "bg_color": arcade.color.CHARCOAL,
            "start_x": SCREEN_WIDTH / 2 - 148,
            "start_y": SCREEN_HEIGHT / 2 - 290,
            "border_width": 0,
            "text_margin": 1,
            "align": "left",
            "anchor_x": "left",
            "anchor_y": "center",
        }

        # create new layout for widget
        self.selection_box = arcade.gui.UIBoxLayout(vertical=True)

        # create button
        push_to_main_text = "$ git push -f origin main"
        push_to_main = arcade.gui.UIFlatButton(
            text=push_to_main_text, width=230, height=30, style=git_style
        )

        # add button to widget layout
        self.selection_box.add(push_to_main.with_space_around(0, 0, 0, 0))

        # on click, set variable selected_gun to selected_text
        # selected_text is defined by clicking on the boxes
        # TODO need to return this variable back to the main game window
        @push_to_main.event("on_click")
        def on_click_push_to_main(event):  # noqa F811: doesn't work when re-defined
            self.selected_gun = available_guns[self.selected_text]
            self.score -= self.selected_gun.price

            self.pause_view.score = self.score
            self.pause_view.equipped_gun = self.selected_gun
            self.pause_view.guns[self.selected_gun.gun_name] = self.selected_gun
            self.all_sprites.append(self.selected_gun)
            self.pause_view.all_sprites = self.all_sprites
            print(f"{self.selected_gun=},{self.score=}")

        # add layouts to GUI manager
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box,
                align_x=0,
                align_y=-100,
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.selection_box,
                anchor_x="left",
                anchor_y="center",
                align_x=SCREEN_WIDTH / 2 - 150,
                align_y=SCREEN_HEIGHT / 2 - 290,
            )
        )

    def on_draw(self):
        """Create displayed elements at the start."""
        arcade.start_render()

        # background
        arcade.draw_lrtb_rectangle_filled(
            left=0,
            right=SCREEN_WIDTH,
            top=SCREEN_HEIGHT,
            bottom=0,
            color=arcade.color.BLACK,
        )
        # 'terminal' box
        arcade.draw_lrtb_rectangle_filled(
            left=SCREEN_WIDTH / 2 - 150,
            right=SCREEN_WIDTH / 2 + 150,
            top=SCREEN_HEIGHT - 220,
            bottom=SCREEN_HEIGHT - 350,
            color=arcade.color.BLACK_LEATHER_JACKET,
        )
        arcade.draw_lrtb_rectangle_filled(
            left=SCREEN_WIDTH / 2 - 148,
            right=SCREEN_WIDTH / 2 + 148,
            top=SCREEN_HEIGHT - 222,
            bottom=SCREEN_HEIGHT - 348,
            color=arcade.color.CHARCOAL,
        )

        # Main welcome screen message
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
        # Display current score
        arcade.draw_text(
            vendor_text,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 150,
            arcade.color.ORANGE,
            font_size=30,
            anchor_x="center",
            bold=True,
        )
        # Give hint to player for return to pause screen
        arcade.draw_text(
            "Press P to return to Pause Screen",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 200,
            arcade.color.ORANGE,
            font_size=20,
            anchor_x="center",
        )

        # 'terminal' commands
        purchase_text = f"$ git add {self.selected_text:15}"
        arcade.draw_text(
            purchase_text,
            SCREEN_WIDTH / 2 - 148,
            SCREEN_HEIGHT - 250,
            arcade.color.CHARTREUSE,
            font_size=15,
            width=10,
            anchor_x="left",
        )
        arcade.draw_text(
            "$ git commit --no-verify",
            SCREEN_WIDTH / 2 - 148,
            SCREEN_HEIGHT - 270,
            arcade.color.CHARTREUSE,
            font_size=15,
            width=10,
            anchor_x="left",
        )

        self.manager.draw()
        self.update(0.0001)

    def on_key_press(self, symbol, modifiers):
        """Return to Pause screen on 'P' press."""
        if symbol == arcade.key.P:
            self.pause_view.on_draw()
            self.window.show_view(self.pause_view)

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
