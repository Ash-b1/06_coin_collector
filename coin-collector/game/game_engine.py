"""
GameEngine: owns the player and all coins.

Starter version: one coin type, no obstacles, no timer yet. Coin
collection also has a known bug (see how `update` uses check_collection
below) that Task 1 asks you to fix - collected coins are never removed,
so standing on one keeps awarding points every frame.
"""

import random
import pygame

from game.player import Player
from game.coin import Coin
from game.collection import check_collection
from game.renderer import WIDTH, HEIGHT
from game.obstacle import Obstacle

NUM_COINS = 6
COIN_TYPES = [
    {"color": (205, 127, 50), "value": 1},   # Bronze
    {"color": (192, 192, 192), "value": 3},  # Silver
    {"color": (255, 215, 0), "value": 5}     # Gold
]

NUM_OBSTACLES = 5

class GameEngine:
    def __init__(self):
        self.player = Player(x=WIDTH / 2, y=HEIGHT / 2)
        self.coins = [self._random_coin() for _ in range(NUM_COINS)]
        self.obstacles = [self._random_obstacle()for _ in range(NUM_OBSTACLES)]
        self.game_over = False
        self.score = 0

    def _random_coin(self):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)

        coin_type = random.choice(COIN_TYPES)

        return Coin(x=x, y=y, radius=12, value=coin_type["value"], color=coin_type["color"])

    def _random_obstacle(self):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)

        return Obstacle(x=x, y=y, size=25)

    def handle_input(self, keys_pressed):
        dx = dy = 0
        if keys_pressed[pygame.K_UP]:
            dy -= self.player.speed
        if keys_pressed[pygame.K_DOWN]:
            dy += self.player.speed
        if keys_pressed[pygame.K_LEFT]:
            dx -= self.player.speed
        if keys_pressed[pygame.K_RIGHT]:
            dx += self.player.speed
        self.player.move(dx, dy, WIDTH, HEIGHT)

    def update(self):
        if self.game_over:
            return
        
        collected = check_collection(self.player, self.coins)
        for coin in collected:
            self.score += coin.value
            self.coins.remove(coin)
        
        for obstacle in self.obstacles:
            if self.player.get_rect().colliderect(obstacle.get_rect()):
                self.game_over = True
                self.coins.clear()
                self.obstacles.clear()

                break

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.player, self.coins,self.obstacles, self.game_over)
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
