# ADR-001: Region-based spatial world model

## Status

Approved.

## Context and problem

Dronesim starts with a discrete grid to simplify simulation development and
mathematical reasoning. Spatial entities such as walls, and spatial effects
such as environmental influence, may span or affect multiple cells. Modeling a
coherent entity as a separate object attached to every affected cell would
fragment that entity's representation.

## Requirements and constraints

- Keep the initial world as a discrete grid.
- Define spatial objects and regions independently of individual cells.
- Allow an object to occupy multiple cells and an effect to extend beyond its
  object's physical footprint.
- Allow effect intensity to vary with distance.
- Allow different spatial properties to use separate data structures.
- Support location queries that may combine information from multiple regions
  or layers.
- Do not prescribe a particular indexing, storage, or effect-calculation
  implementation.

## Alternatives considered

- **One independent object per affected cell:** rejected for coherent spatial
  entities because it fragments objects such as a wall spanning a range.
- **Cell-only representation of spatial effects:** not selected as the sole
  representation, since an effect may be defined by a region and extend beyond
  an object's footprint. Per-cell storage remains a possible implementation
  technique.
- **Regions and objects defined independently of cells:** selected as the
  spatial representation; it can describe entities spanning cells and effects
  extending into surrounding cells.

## Decision

Represent spatial objects and regions independently of individual grid cells.
An object may occupy multiple cells; a spatial effect may extend beyond the
object's physical footprint and vary in intensity with distance. Spatial
properties may use separate data structures, and a location query may combine
information from multiple regions or layers.

This decision does not reject dense per-cell arrays, cached values, or other
cell-based techniques as implementation choices.

## Developer's rationale

The developer rejected representing a coherent object such as a wall as
separate objects attached to every affected cell. A wall should be representable
as one spatial entity spanning a range. Likewise, a circular environmental
region may be described by a center and radius, with influence extending into
surrounding cells. The discrete grid is the initial choice to simplify
simulation development and mathematical reasoning.

## Optimization objectives

The representation is intended to preserve coherent spatial entities, express
effects beyond physical footprints, and allow distinct spatial properties to
be represented separately. These are design objectives, not measured
performance results. The initial grid is intended to keep early simulation
development simple.

## Accepted disadvantages

- Resolving which regions or objects affect a location, and combining their
  information, requires defined query behavior.
- Mapping region geometry and distance-varying effects onto a discrete grid
  requires implementation choices that are not settled by this decision.
- Keeping spatial entities independent of cells does not by itself determine
  the best storage or query performance.

## Assumptions and risks

- The initial simulation uses discrete grid coordinates even when a region is
  described geometrically, such as by a center and radius.
- The appropriate representation and query behavior may differ by spatial
  property.
- Continuous geometry represented on a discrete grid may limit fidelity; the
  degree of that tradeoff is not yet established.

## Conditions for reconsideration

Reconsider this decision if requirements for spatial behavior change, if
experience with the initial model shows that it cannot express needed
properties or queries, or if measured results show that the chosen approach
does not meet project needs. Reconsideration requires developer approval.

## Explicitly unresolved implementation decisions

This ADR does not approve or select:

- Cell-to-object spatial indexes or chunk-based indexes.
- Eager or lazy index maintenance.
- Caching or precomputing spatial effects.
- A distance metric, falloff function, or rule for aggregating overlapping
  fields.
- Exact region classes, object interfaces, or query interfaces.

These approaches remain open for later design decisions. Dense per-cell storage
and cached spatial values remain possible techniques; this ADR rejects only
fragmenting a coherent spatial object into independent per-cell objects as the
representation of that object.
