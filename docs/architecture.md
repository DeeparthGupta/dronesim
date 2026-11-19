# Architecture

## Purpose

Dronesim is a Python simulation project. Its current application is a small,
interactive grid-world prototype built with Pygame.

## Current implementation

The application defines a `World` with positive integer `height` and `width`
values. `World.contains()` checks `(x, y)` positions against half-open bounds.
The Pygame viewer defaults to a 10-by-10 world and accepts independent
`--width` and `--height` command-line options. Cell size is configurable with
`--cell-side` and defaults to 32 pixels. The viewer draws a grid sized to the
world and lets the user move a cursor one cell at a time with the arrow keys.
The cursor is kept in the application loop, separately from the `World`, which
stores only dimensions. See [`main.py`](../src/dronesim/main.py#L19) for
`World`, [`main.py`](../src/dronesim/main.py#L54) for argument parsing, and
[`main.py`](../src/dronesim/main.py#L61) for grid rendering.

The implementation does not yet store cell properties, spatial objects or
regions, agents, or observations. Integer dimensions and coordinates are an
approved contract. Dimensions are validated as positive integers; position
types are not validated by `World.contains()`.

## Established architectural decisions

These are design constraints, not claims that the corresponding functionality
already exists:

- Start with a discrete, rectangular grid whose dimensions are fixed at
  creation. Coordinates are integer `(x, y)` pairs with origin at the top-left.
- Keep world state independent from visualization state. The world is the
  authoritative source of complete state; agents should use observations and
  locally available information, which may be incomplete or stale. A
  visualizer may show information unavailable to agents.
- Allow different world properties to use separate data structures. Define
  spatial objects and regions independently of individual cells; objects may
  occupy multiple cells, and spatial effects may extend beyond an object's
  footprint and vary in intensity with distance. A location query may combine
  multiple properties or regions.
- Prefer a simple gridworld and preserve immediate visual feedback during
  development. NumPy was deliberately omitted from the initial implementation.

## Unresolved design questions

The initial world-state representation and cell-query interface are undecided.
The representation of regions, spatial effects, and combined location queries
also remains open. Agent behavior and simulation scheduling have not been
decided.

The following approaches remain tentative, not approved implementation
decisions: cell-to-object or chunk-based indexes; eager or lazy index
maintenance; spatial-property caching or precomputed fields; specific region
geometry; rich terrain objects versus enumerated terrain types; behavior trees,
state machines, or utility-based policies; scheduling strategies; and
communication or consensus protocols.

## Long-term objectives (nonbinding)

Dronesim may eventually support heterogeneous autonomous agents, zones of
interest, charging infrastructure, mission orchestration, autonomous behavior
during communication loss, simulated networks and network partitions, failures,
partial observability, distributed coordination and consensus, and reproducible
experiments. Continuous spatial models and more realistic dynamics are also
long-term objectives. These aspirations are not current implementation
requirements or decisions to add abstractions now.
