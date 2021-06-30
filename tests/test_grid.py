# test/test_grid.py

from kallisto.grid import getLebedevLaikovGrid, gridSize


def test_user_can_create_grid_sizes():
    for n in range(23):
        size = gridSize[n]
        grid, weights = getLebedevLaikovGrid(n)
        if len(weights) != size:
            raise AssertionError
        if len(grid[:, 1]) != size:
            raise AssertionError
        if len(grid[1, :]) != 3:
            raise AssertionError
