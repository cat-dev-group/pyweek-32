import arcade


class Gun(arcade.Sprite):
    """
    Base sprite for guns.
    """

    # def __init__(self, gun: str, *args, **kwargs) -> None:
    #     self.guns = {
    #         "py-90": {
    #             "ammo": 75,
    #             "rof": 7,
    #             "mag_size": 20,
    #             "specialty": ErrorType.PYTHON,
    #             "price": "DEFAULT",
    #             "image": "src/images/MP5.png",
    #         },
    #         "stdlib-15": {
    #             "ammo": 50,
    #             "rof": 3,
    #             "mag_size": 10,
    #             "specialty": ErrorType.STDLIB,
    #             "price": 50,
    #             "image": "src/images/APS.png",
    #         },
    #     }
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

        # if self.guns.get(gun) is None:
        #     raise TypeError(f"Invalid gun {gun} provided")

        # self.unlocked_guns = ["py-90"]
        # self.equipped_gun = self.guns[gun]

        super().__init__(self.image, *args, **kwargs)

    # def add_gun(self, gun: str) -> None:
    #     if self.guns.get(gun) is None:
    #         raise TypeError(f"Invalid gun {gun} provided")

    #     self.unlocked_guns.append(gun)

    # def equip_gun(self, gun: str) -> None:
    #     if gun not in self.unlocked_guns:
    #         raise RuntimeError(f"Gun {gun} is not unlocked or does not exist")

    #     self.equipped_gun = self.guns[gun]

    # def get_price(self, gun: str) -> int:
    #     if self.guns.get(gun) is None:
    #         raise TypeError(f"Invalid gun {gun} provided")

    #     return self.guns[gun]["price"]
