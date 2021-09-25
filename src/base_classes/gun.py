import arcade


class Gun(arcade.Sprite):
    """
    Base sprite for guns.
    """

    def __init__(
        self, gun_name, ammo, rof, mag_size, specialty, price, image, *args, **kwargs
    ) -> None:

        self.gun_name = gun_name
        self.ammo = ammo
        self.rof = rof
        self.mag_size = mag_size
        self.specialty = specialty
        self.price = price
        self.image = image

        super().__init__(self.image, *args, **kwargs)
