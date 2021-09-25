import arcade


class FlyingEnemy(arcade.Sprite):
    """Base class for moving enemies."""

    def __init__(self, health, *args, **kwargs) -> None:
        self.health = health
        super().__init__(*args, **kwargs)

    def update(self):
        """
        Update the position of the enemy.
        When it moves off the bottom of the screen, remove it.
        """

        super().update()

        # remove the enemy if it goes off screen
        if self.top < 0:
            self.remove_from_sprite_lists()
