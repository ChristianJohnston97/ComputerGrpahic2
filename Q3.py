#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under the MIT License
    Developed by Onur Ra ates the following operations:
    * Generating a control points grid
    * Rotating the control points grid about some chosen axes
    * Generating a B-Spline surface and using the generated grid as its control points input
    * Plotting the surface
"""

from geomdl import tessellate
from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities

from geomdl.visualization import VisMPL as myvis
# from geomdl.visualization import VisPlotly as myvis

# Generate a control points grid
surfgrid = CPGen.Grid(50, 100)

# Grid size 25x30
surfgrid.generate(25, 30)

# Generate bumps on the grid
surfgrid.bumps(num_bumps=5, bump_height=20, base_extent=4)

surfgrid.bumps(num_bumps=1, bump_height=60, base_extent=4)


# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Get the control points from the generated grid
surf.ctrlpts2d = surfgrid.grid

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# Set sample size of the split surface
surf.sample_size = 50

# Generate the visualization component and its configuration
vis_config = myvis.VisConfig(ctrlpts=False, legend=False)
vis_comp = myvis.VisSurfTriangle(vis_config)

# Set visualization component of the split surface
surf.vis = vis_comp

# Plot the split surface
surf.render()

# Good to have something here to put a breakpoint
pass