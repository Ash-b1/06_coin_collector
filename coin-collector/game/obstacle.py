import pygame


class Obstacle:
    def __init__(self, x, y, size=25):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 0, 0)

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.size),
            int(self.y - self.size),
            self.size * 2,
            self.size * 2
        )

    def get_points(self):
        return [
            (int(self.x), int(self.y - self.size)),       # top
            (int(self.x - self.size), int(self.y + self.size)),  # bottom-left
            (int(self.x + self.size), int(self.y + self.size))   # bottom-right
        ]