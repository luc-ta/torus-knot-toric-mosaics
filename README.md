# torus-knot-toric-mosaics
Install the ortools Python package before use: https://pypi.org/project/ortools/

This program generates upper bounds on the toric mosaic numbers of (p, q) torus knots. (For more information on toric knot mosaics, see https://arxiv.org/pdf/1206.4227 or https://arxiv.org/pdf/1703.04867.)

Specifically, it runs an integer linear programming (ILP) algorithm to compute non-negative integer solutions (h, v) to a system of inequalities determined in an in-progress research paper. Then, it chooses a solution that minimizes n := q-h-v, where h(p-1) is the number of horizontal crossings and v(p-1) is the number of vertical crossings. The program is adapted from https://developers.google.com/optimization/mip/mip_example.
