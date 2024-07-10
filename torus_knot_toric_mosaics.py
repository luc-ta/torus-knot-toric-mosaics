# -*- coding: utf-8 -*-
"""
Created on Mon Jul 8 19:03:12 2024

@author: Luc Ta
"""

from ortools.linear_solver import pywraplp


def main():
    
    print("Please enter p.")
    p = int(input())
    
    print("Please enter q such that p < q and gcd(p,q) = 1.")
    q = int(input())
    
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SAT")
    if not solver:
        return

    infinity = solver.infinity()
    # Make h and v non-negative integer variables
    h = solver.IntVar(0.0, infinity, "h")
    v = solver.IntVar(0.0, infinity, "v")

    # First constraint
    solver.Add(-3 * h - v - p + q + 4 >= 0)

    # Second constraint: r >= -R
    solver.Add(q - 2 * (h + v + p) + 4 >= 0)
    
    # Third constraint: R >= r
    solver.Add(h + 3 * v <= q - 3 * p + 4)
    
    # Fourth constraint
    solver.Add(h >= v)

    # Optimize n, the size of the toric mosaic.
    solver.Minimize(q - h - v)

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution minimizing n := q - h - v:")
        print("n =", solver.Objective().Value())
        print("h =", h.solution_value())
        print("v =", v.solution_value())
        print("Total horizontal crossings:", (p - 1) * h.solution_value())
        print("Total vertical crossings:", (p - 1) * v.solution_value())

    else:
        print("The problem does not have an optimal solution.")

if __name__ == "__main__":
    main()
