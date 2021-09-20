from dataclasses import dataclass

@dataclass
class Gun:
    """Dataclass for implementing guns in the game."""
    name: str
    mag_size: int
    reload_time: int
    bullets_per_shot: int
    shots_per_second: int
    path_to_sprite: str
    explosive_bullets: bool = False
