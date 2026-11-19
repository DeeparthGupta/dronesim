import contextlib
import io
import unittest

import pygame

from dronesim.main import GRID_COLOR, World, draw_grid, parse_args


class WorldDimensionTests(unittest.TestCase):
    def test_cli_defaults_to_ten_by_ten(self):
        args = parse_args([])

        self.assertEqual((args.width, args.height), (10, 10))
        self.assertEqual(args.cell_side, 32)

    def test_cli_accepts_independent_dimensions(self):
        args = parse_args(
            ["--width", "13", "--height", "7", "--cell-side", "24"]
        )

        self.assertEqual((args.width, args.height), (13, 7))
        self.assertEqual(args.cell_side, 24)

    def test_cli_defaults_unspecified_dimension_independently(self):
        args = parse_args(["--width", "13"])

        self.assertEqual((args.width, args.height), (13, 10))

    def test_cli_rejects_non_positive_or_non_integer_dimensions(self):
        for option in ("--width", "--height", "--cell-side"):
            for value in ("0", "-1", "1.5"):
                with (
                    self.subTest(option=option, value=value),
                    contextlib.redirect_stderr(io.StringIO()),
                    self.assertRaises(SystemExit) as error,
                ):
                    parse_args([option, value])

                self.assertEqual(error.exception.code, 2)

    def test_world_requires_positive_integer_dimensions(self):
        invalid_dimensions = ((0, 1), (-1, 1), (1.5, 1), (True, 1))

        for height, width in invalid_dimensions:
            with self.subTest(height=height, width=width), self.assertRaises(
                ValueError
            ):
                World(height=height, width=width)


class GridRenderingTests(unittest.TestCase):
    def test_horizontal_grid_lines_span_rectangular_world_width(self):
        cell_side = 32
        world = World(height=7, width=13)
        surface = pygame.Surface((world.width * cell_side, world.height * cell_side))

        draw_grid(surface, world, cell_side)

        pixel_x = world.height * cell_side + 10
        self.assertEqual(surface.get_at((pixel_x, cell_side)), GRID_COLOR)
