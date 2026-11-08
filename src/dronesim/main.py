import pygame

MOVEMENT_KEYS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, 1),
    pygame.K_DOWN: (0, -1),
}


class World:
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise ValueError("Dimensions cannot be 0 or lower")

        self.height = height
        self.width = width

    def is_valid(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height


def cell_rect(x, y, cell_side):
    # Convert world coordinates to a pixel rectangle.
    return pygame.Rect(x * cell_side, y * cell_side, cell_side, cell_side)


def main():
    world = World(height=10, width=10)
    cell_side = 2

    pygame.init()

    screen = pygame.display.set_mode(
        (world.width * cell_side, world.height * cell_side)
    )
    pygame.display.set_caption("DroneSim")

    cursor = (0, 0)

