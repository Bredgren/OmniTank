#!/usr/bin/env python
"""Tank classes."""
import math
import pygame

def clamp(n, minimum, maximum):
    """Clamps n to be between minimum and maximum."""
    return min(maximum, max(minimum, n))

def sign(n):
    """Return the sign of n."""
    return 1 if n > 0 else -1 if n < 0 else 0

class Tank(pygame.sprite.Sprite): # pylint: disable=too-many-instance-attributes
    """Base Tank class for both player and enemies."""
    DAMAGE = 0
    SPEED = 0
    ACCELERATION = 0
    TURN_SPEED = 0
    RELOAD_TIME = 0

    FRICTION = 1

    def __init__(self, image, bounds, max_hp):
        super().__init__()
        self.image = image
        # Keep a copy of the original so we don't lose quality from repeated rotations
        self.src_image = image
        self.bounds = bounds
        self.rect = self.image.get_rect()
        self.position = (0, 0)
        self.speed = {
            "x": 0,
            "y": 0,
        }
        self.rotation = 0

        self.max_hp = max_hp
        self.hp = self.max_hp

        self.move = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "turn_left": False,
            "turn_right": False,
        }

    def move_to(self, position):
        """Move the tank to the given position."""
        self.position = position
        self.rect.center = self.position

    def update(self):
        """Per frame update method."""
        raise NotImplementedError()

    def update_movement(self):
        """Updates the tank's speed/rotation."""
        self.speed["x"] += (self.move["right"] - self.move["left"]) * self.ACCELERATION
        self.speed["x"] -= self.FRICTION * sign(self.speed["x"])
        self.speed["x"] = clamp(self.speed["x"], -self.SPEED, self.SPEED)

        self.speed["y"] += (self.move["forward"] - self.move["backward"]) * self.ACCELERATION
        self.speed["y"] -= self.FRICTION * sign(self.speed["y"])
        self.speed["y"] = clamp(self.speed["y"], -self.SPEED, self.SPEED)

        self.rotation += (self.move["turn_left"] - self.move["turn_right"]) * self.TURN_SPEED
        x, y = self.position
        rad = math.radians(self.rotation)
        x += self.speed["x"] * math.cos(rad) - self.speed["y"] * math.sin(rad)
        y += -self.speed["x"] * math.sin(rad) - self.speed["y"] * math.cos(rad)
        self.rotation %= 360

        wrap_offset = 50
        x = ((x + wrap_offset) % (self.bounds.width + wrap_offset * 2)) - wrap_offset
        y = ((y + wrap_offset) % (self.bounds.height + wrap_offset * 2)) - wrap_offset

        # Move to new position
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def deal_damage(self, amount):
        """Deal a damage of amount to the tank."""
        self.hp -= amount

    def _check_for_death(self):
        if self.hp <= 0:
            self.kill()

    def draw(self, screen):
        """Extra draw funtionality."""
        raise NotImplementedError()

class Player(Tank):
    """The player-controlled tank."""
    MAX_HP = 500
    DAMAGE = 10
    SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 200

    def __init__(self, image, bounds):
        super().__init__(image, bounds, self.MAX_HP)

    def update(self):
        self.update_movement()
        self._check_for_death()

    def draw(self, screen):
        pass

class EnemyTank(Tank):
    """The base for enemy tanks."""
    FIRST_LEVEL = 0
    IMAGE = None
    BASE_HP = 0
    POINTS = 0

    def __init__(self, bounds, player, level):
        super().__init__(self.IMAGE, bounds, self.get_max_hp(level))
        self.player = player
        self.player_pos = (0, 0)
        self.player_rot = 0

    def get_max_hp(self, level):
        """Returns ths max hp for the tank at the given the game level."""
        return self.BASE_HP + ((int(level) - self.FIRST_LEVEL) * 5)

    def update(self):
        self.ai()
        self.update_movement()
        self._check_for_death()

    def control(self):
        """Decides how the tank should move."""
        raise NotImplementedError()

    def draw(self, screen):
        self._draw_hp(screen)

    def _draw_hp(self, screen):
        x = self.position[0] - 50
        y = self.position[1] - 60
        screen.fill((255, 0, 0), (x, y, 50, 5))
        screen.fill((0, 255, 0), (x, y, (self.hp / self.max_hp) * 50, 5))

    def angle_to_player(self):
        """The counter-clockwise angle off -y axis that points toward the player"""
        dx = self.position[0] - self.player.position[0]
        dy = self.position[1] - self.player.position[1]
        return math.degrees(math.atan2(dx, dy)) % 360

    def _basic_movement(self, min_dist, max_dist):
        x, y = self.position
        player_x, player_y = self.player.position
        dist_to_player = math.sqrt((player_x - x) ** 2 + (player_y - y) ** 2)

        angle = self.angle_to_player()
        angle_dist = abs(angle - self.rotation)

        self.move["turn_right"] = False
        if 6 <= angle_dist < 180:
            self.move["turn_right"] = angle <= angle_dist
        elif angle_dist >= 180:
            self.move["turn_right"] = angle > angle_dist
        else:
            # Forward/back movement
            self.move["backward"] = dist_to_player < min_dist
            self.move["forward"] = dist_to_player > max_dist
        self.move["turn_left"] = not self.move["turn_right"]

    def _omni_movement(self):
        x, y = self.position
        player_x, player_y = self.player.position
        player_dir = self.player.rotation
        dist_to_player = math.sqrt((player_x - x) ** 2 + (player_y - y) ** 2)

        # Left/right movement
        self.move["right"] = False
        if x < player_x:
            if y < player_y:
                self.move["right"] = player_dir < 45
            else:
                self.move["right"] = player_dir > 90 and player_dir < 135
        else:
            if y < player_y:
                self.move["right"] = player_dir < 315
            else:
                self.move["right"] = player_dir < 270 and player_dir > 225
        self.move["left"] = not self.move["right"]

        # Forward/back movement
        self.move["backward"] = dist_to_player < 300
        self.move["forward"] = dist_to_player > 400

        # Turning
        angle = self.angle_to_player()
        angle_dist = abs(angle - self.rotation)

        self.move["turn_right"] = ((6 <= angle_dist < 180 and angle <= angle_dist) or
                                   (angle_dist >= 180 and angle > angle_dist))
        self.move["turn_left"] = ((6 <= angle_dist < 180 or angle_dist >= 180) and
                                  not self.move["turn_right"])

class SaucerEnemy(EnemyTank):
    """The saucer enemy."""
    FIRST_LEVEL = 1
    BASE_HP = 30
    DAMAGE = 5
    SPEED = 5
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 1500
    POINTS = 10

    def control(self):
        self._omni_movement()

class TriangleEnemy(EnemyTank):
    """The triangle enemy."""
    FIRST_LEVEL = 2
    BASE_HP = 10
    DAMAGE = 10
    SPEED = 3
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 1500
    POINTS = 20

    def control(self):
        self._basic_movement(100, 200)

class TankEnemy(EnemyTank):
    """The tank enemy."""
    FIRST_LEVEL = 3
    BASE_HP = 50
    DAMAGE = 20
    SPEED = 1
    ACCELERATION = 2
    TURN_SPEED = 4
    RELOAD_TIME = 5000
    POINTS = 50

    def control(self):
        self._basic_movement(400, 500)

class MineEnemy(EnemyTank):
    """The mine enemy."""
    FIRST_LEVEL = 4
    BASE_HP = 40
    DAMAGE = 50
    SPEED = 4
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 3000
    POINTS = 30

    def control(self):
        pass

class TrishotEnemy(EnemyTank):
    """The trishot enemy."""
    FIRST_LEVEL = 5
    BASE_HP = 40
    DAMAGE = 20
    SPEED = 3
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 2000
    POINTS = 60

    def control(self):
        self._basic_movement(350, 450)

class BossEnemy(EnemyTank):
    """The boss enemy."""
    FIRST_LEVEL = 1
    BASE_HP = 70
    DAMAGE = 10
    SPEED = 15
    ACCELERATION = 2
    TURN_SPEED = 6
    RELOAD_TIME = 1000
    POINTS = 200

    def control(self):
        self._omni_movement()
