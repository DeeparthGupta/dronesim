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
        if height <= 0 or width <= 0:
            raise ValueError("Dimensions cannot be 0 or lower")

        self.height = height
        self.width = width

    def contains(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height


def cell_rect(x, y, cell_side):
    # Convert world coordinates to a pixel rectangle.
    return pygame.Rect(x * cell_side, y * cell_side, cell_side, cell_side)


def main():
    world = World(height=10, width=10)
    cell_side = 32

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

            # Draw grid lines
            for x in range(world.width + 1):
                px = x * cell_side
                pygame.draw.line(
                    screen, GRID_COLOR, (px, 0), (px, world.height * cell_side)
                )

            for y in range(world.height + 1):
                py = y * cell_side
                pygame.draw.line(
                    screen, GRID_COLOR, (0, py), (world.height * cell_side, py)
                )

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
