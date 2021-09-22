import random

import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SCREAMING_SNAKE_SHOOTER"
SCALING = 1.0


class FlyingEnemy(arcade.Sprite):
    """Base class for moving enemies."""

    def update(self):
        """Update the position of the enemy.
        When it moves off the bottom of the screen, remove it.
        """

        # I like to move it move it
        super().update()

        # remove the enemy
        if self.top < 0:
            self.remove_from_sprite_lists()


class SnakeShooter(arcade.Window):
    """SCREAMING_SNAKE_SHOOTER is a top-down survival shooter game."""

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # define a list of enemies as a SpriteList
        self.enemies_list = arcade.SpriteList()
        # TODO
        # add background / guns / bullets or other SpriteLists
        # a list to hold all sprites
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Set up the game."""

        # placeholder for the background, choosing a default color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # placeholder for the player, using built in space ship for now
        ship_image = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player = arcade.Sprite(ship_image, SCALING)
        self.player.bottom = 10  # set the initial position 10 pixels from the bottom
        self.player.center_x = (
            self.width / 2
        )  # set the initial position in the middle of the screen
        self.all_sprites.append(self.player)

        # Scheduling Functions
        # TODO need to add some logic to define when / how to "spawn" enemies
        # schedule accepts an addition function for adding a sprite
        # and a time between adding enemies
        arcade.schedule(self.add_enemy, 0.5)

        self.paused = False

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen.

        params:
            delta_time (float): How much time has passed since the last call
        """
        # placeholder for enemy, using built in bee for now
        enemy_image = ":resources:images/enemies/bee.png"
        enemy = FlyingEnemy(enemy_image, SCALING)

        # set position to above the screen, at a random width
        enemy.bottom = random.randint(self.height, self.height + 80)
        enemy.right = random.randint(10, self.width - 10)

        # velocity is a list of the form x,y
        # with enemies coming straight down, change in x is 0
        enemy.velocity = (0, random.randint(-20, -5))

        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def on_key_press(self, symbol, modifiers):
        """Handle user input.
        Q: Quit
        P: Pause
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
            self.paused = not self.paused

        # Commenting out for now, should the player be able to move up or down?
        # if symbol == arcade.key.W or symbol == arcade.key.UP:
        #     self.player.change_y = 5

        # if symbol == arcade.key.S or symbol == arcade.key.DOWN:
        #     self.player.change_y = -5

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -5

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        params:
            symbol (int): Which key was pressed
            modifiers (int): Which modifiers were pressed
        """
        # Commenting out for now, should the player be able to move up or down?
        # if (
        #     symbol == arcade.key.W
        #     or symbol == arcade.key.S
        #     or symbol == arcade.key.UP
        #     or symbol == arcade.key.DOWN
        # ):
        #     self.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions of all game objects.
        If paused, do nothing.

        params:
            delta_time (float): Time since the last update
        """
        # Check for pause
        if self.paused:
            return

        # Update everything
        self.all_sprites.update()

        # Check player position
        # commenting out the top and bottom for now
        # if self.player.top > self.height:
        #     self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        # # if self.player.bottom < 0:
        # #     self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Draw all game objects."""
        arcade.start_render()
        self.all_sprites.draw()


if __name__ == "__main__":
    screaming_snake_shooter = SnakeShooter(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )
    screaming_snake_shooter.setup()
    arcade.run()
