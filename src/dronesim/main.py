import argparse

import pygame

MOVEMENT_KEYS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
}

# Colors
BACKGROUND_COLOR = pygame.Color("#191C23")
GRID_COLOR = pygame.Color("#414650")
CURSOR_COLOR = pygame.Color("#3C96F0")
CURSOR_BORDER_COLOR = pygame.Color("#B4DCFF")


class World:
    def __init__(self, height, width):
        if (
            not isinstance(height, int)
            or isinstance(height, bool)
            or not isinstance(width, int)
            or isinstance(width, bool)
            or height <= 0
            or width <= 0
        ):
            raise ValueError("Dimensions must be positive integers")

        self.height = height
        self.width = width

    def contains(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height


def cell_rect(x, y, cell_side):
    # Convert world coordinates to a pixel rectangle.
    return pygame.Rect(x * cell_side, y * cell_side, cell_side, cell_side)


def positive_integer(value):
    try:
        dimension = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error

    if dimension <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")

    return dimension


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=positive_integer, default=10)
    parser.add_argument("--height", type=positive_integer, default=10)
    parser.add_argument("--cell-side", type=positive_integer, default=32)
    return parser.parse_args(argv)


def draw_grid(screen, world, cell_side):
    for x in range(world.width + 1):
        px = x * cell_side
        pygame.draw.line(screen, GRID_COLOR, (px, 0), (px, world.height * cell_side))

    for y in range(world.height + 1):
        py = y * cell_side
        pygame.draw.line(screen, GRID_COLOR, (0, py), (world.width * cell_side, py))


def main():
    args = parse_args()
    world = World(height=args.height, width=args.width)
    cell_side = args.cell_side

    pygame.display.init()

    screen = pygame.display.set_mode(
        (world.width * cell_side, world.height * cell_side)
    )
    pygame.display.set_caption("DroneSim")

    clock = pygame.Clock()
    cursor = (0, 0)

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type != pygame.KEYDOWN:
                    continue

                direction = MOVEMENT_KEYS.get(event.key)
                if direction is None:
                    continue

                # Calculate the new position
                x, y = cursor
                dx, dy = direction
                candidate_position = (x + dx, y + dy)

                # Set cursor to new location if valid
                if world.contains(candidate_position):
                    cursor = candidate_position

            screen.fill(BACKGROUND_COLOR)

            draw_grid(screen, world, cell_side)

            # Highlight cursor cell
            x, y = cursor
            rect = cell_rect(x, y, cell_side)

            pygame.draw.rect(screen, CURSOR_COLOR, rect)
            pygame.draw.rect(screen, CURSOR_BORDER_COLOR, rect, 2)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
