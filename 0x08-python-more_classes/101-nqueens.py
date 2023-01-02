#!/usr/bin/python3
'''Module for nquens task'''
import sys


def solve_nqueens(n, queens, xy_diffs, xy_sums):
    p = len(queens)
    if p == n:
        # Print the solution in the desired format
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(i, queens[i]), end="")
            if i < n - 1:
                print(", ", end="")
        print("]")
        return
    for q in range(n):
        if q not in queens and p - q not in xy_diffs and p + q not in xy_sums:
            solve_nqueens(n,
                          queens + [q],
                          xy_diffs + [p - q],
                          xy_sums + [p + q])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, [], [], [])


if __name__ == "__main__":
    main()
