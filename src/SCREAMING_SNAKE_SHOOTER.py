import os
import random

import arcade
from dotenv import load_dotenv

from src.base_classes.FlyingEnemy import FlyingEnemy
from src.base_classes.gun import Gun
from src.error_throwing import ErrorType, generate_error
from src.views.PauseView import PauseScreen

load_dotenv()

PLAYER_SCALE = float(os.getenv("PLAYER_SCALE"))
DEFAULT_SCALE = float(os.getenv("DEFAULT_SCALE"))
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT"))


class SnakeShooter(arcade.View):
    """SCREAMING_SNAKE_SHOOTER is a top-down survival shooter game."""

    def __init__(self):
        super().__init__()

        # define a list of enemies as a SpriteList
        self.enemies_list = arcade.SpriteList()
        # TODO
        # add background / guns / bullets or other SpriteLists
        self.bullets_list = arcade.SpriteList()
        # a list to hold all sprites
        self.all_sprites = arcade.SpriteList()

        default_gun = Gun(
            gun_name="default",
            ammo=10000,
            rof=20,
            mag_size=10000,
            specialty=ErrorType.PYTHON,
            price=0,
            image=":resources:images/space_shooter/laserBlue01.png",
            scale=0.5,
            angle=90,
        )
        self.guns = {"default_gun": default_gun}
        self.equipped_gun = self.guns["default_gun"]
        self.gun_index = 0

    def setup(self):
        """Set up the game."""
        arcade.set_background_color(arcade.color.XANADU)

        ship_image = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player = arcade.Sprite(ship_image, PLAYER_SCALE)

        self.equipped_gun.bottom = 15
        self.equipped_gun.center_x = self.player.center_x - 10

        self.player.bottom = 10  # set the initial position 10 pixels from the bottom
        self.player.center_x = (
            SCREEN_WIDTH / 2
        )  # set the initial position in the middle of the screen
        self.all_sprites.append(self.player)
        self.all_sprites.append(self.equipped_gun)

        self.paused = False

        self.score = 0

        # Scheduling Functions
        # schedule accepts an addition function for adding a sprite
        # and a time between adding enemies
        arcade.schedule(self.add_enemy, 0.5)

    def add_enemy(self, delta_time: float):
        """
        Adds a new enemy to the screen.

        params:
            delta_time (float): How much time has passed since the last call
        """
        error = generate_error()
        enemy = FlyingEnemy(
            error.health, f"src/images/{error.error_type.value}_bug.png", error.scale
        )

        # set angle to have the bug speeding down towards the player
        enemy.angle = 180

        # set position to above the screen, at a random width
        enemy.bottom = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 80)
        enemy.right = random.randint(10, SCREEN_WIDTH - 10)

        # velocity is a list of the form x,y
        # with enemies coming straight down, change in x is 0
        enemy.velocity = (0, random.randint(-500, -300))

        # add enemy to enemy list and sprites list
        # will use to check for collisions and update loop
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def add_bullet(self, start_position):
        """Add a bullet when space bar is pressed."""

        bullet_image = ":resources:images/space_shooter/laserBlue01.png"
        bullet = arcade.Sprite(bullet_image, DEFAULT_SCALE)
        bullet.angle = 90.0
        bullet.bottom = self.player.top
        bullet.center_x = start_position

        bullet.velocity = (0, 400)

        # add bullet to bullet list and sprites list
        # will use to check for collisions and update loop
        self.bullets_list.append(bullet)
        self.all_sprites.append(bullet)

    def on_key_press(self, symbol, modifiers):
        """
        Handle user input.
        ESCAPE: Pause (pause in the future, quit immediately now)
        W / A / S / D: Move Up, Left, Down Right
        Arrows: Move Up, Left, Down Right

        params:
            symbol (int): Which key was pressed
            modifiers (int): Which modifiers were pressed
        """
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            pause = PauseScreen(self)
            self.window.show_view(pause)

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -500
            self.equipped_gun.change_x = -500
            self.player.angle = 90

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 500
            self.player.angle = -90
            self.equipped_gun.change_x = 500

        if symbol == arcade.key.SPACE:
            self.add_bullet(self.player.center_x)
            if self.equipped_gun.gun_name == "EX47":
                # can add multiple bullets at once and at different positions
                self.add_bullet(self.player.left)
                self.add_bullet(self.player.right)
            self.player.angle = 0

        if symbol == arcade.key.TAB:
            if self.gun_index not in range(0, len(self.guns) - 1):
                self.gun_index = 0
                next_gun = list(self.guns)[self.gun_index]
                self.equipped_gun.remove_from_sprite_lists()
                self.equipped_gun = self.guns[next_gun]
                print(f"{self.equipped_gun = }")
            else:
                self.gun_index += 1
                next_gun = list(self.guns)[self.gun_index]
                self.equipped_gun.remove_from_sprite_lists()
                self.equipped_gun = self.guns[next_gun]
                print(f"{self.equipped_gun = }")

    def on_key_release(self, symbol: int, modifiers: int):
        """
        Undo movement vectors when movement keys are released

        params:
            symbol (int): Which key was pressed
            modifiers (int): Which modifiers were pressed
        """
        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0
            self.player.angle = 0
            self.equipped_gun.change_x = 0

    def on_update(self, delta_time: float):
        """
        Update the positions of all game objects.
        If paused, do nothing.

        params:
            delta_time (float): Time since the last update
        """
        # Check for collision
        if self.player.collides_with_list(self.enemies_list) or self.score < 0:
            # TODO create end game popup
            arcade.close_window()

        # Check for collision
        for enemy in self.enemies_list:
            for bullet in self.bullets_list:
                if enemy.collides_with_list(self.bullets_list):
                    if enemy.health <= 0 or enemy.scale <= 0.1:
                        enemy.remove_from_sprite_lists()
                    else:
                        enemy.health -= 50
                        enemy.scale -= 0.05
                    bullet.remove_from_sprite_lists()
                    self.score += 100

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(sprite.center_x + sprite.change_x * delta_time)
            sprite.center_y = int(sprite.center_y + sprite.change_y * delta_time)

        # Check player position
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH
        if self.player.left < 0:
            self.player.left = 0
        if self.equipped_gun.right > SCREEN_WIDTH:
            self.equipped_gun.right = SCREEN_WIDTH
        if self.equipped_gun.left < 0:
            self.equipped_gun.left = 0

    def on_draw(self):
        """Draw all game objects."""
        arcade.start_render()
        self.all_sprites.draw()

        arcade.draw_lrtb_rectangle_filled(
            left=SCREEN_WIDTH - 120,
            right=SCREEN_WIDTH,
            top=SCREEN_HEIGHT,
            bottom=SCREEN_HEIGHT - 30,
            color=arcade.color.BLACK,
        )

        score_text = f"COINS: {self.score:9}"
        arcade.draw_text(
            score_text,
            SCREEN_WIDTH - 110,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE,
            10,
        )
