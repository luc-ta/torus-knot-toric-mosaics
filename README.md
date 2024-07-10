# torus-knot-toric-mosaics
Install the ortools Python package before use: https://pypi.org/project/ortools/

This program generates upper bounds on the toric mosaic numbers of (p, q) torus knots. (For more information on toric knot mosaics, see https://arxiv.org/pdf/1206.4227 or https://arxiv.org/pdf/1703.04867.)

Specifically, given a torus knot (p, q), the program runs an integer linear programming (ILP) algorithm to compute non-negative integer solutions (h, v) to a system of inequalities determined in a forthcoming research paper. Then, it chooses a solution that minimizes n := q-h-v, where h(p-1) is the number of horizontal crossings and v(p-1) is the number of vertical crossings. As the paper will show, choice of n is an upper bound on the toric mosaic number of (p, q). The program is adapted from https://developers.google.com/optimization/mip/mip_example.
