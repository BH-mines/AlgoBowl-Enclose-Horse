from enclose_horse import parse_input
from tile_score import tile_score
from enclose_horse import bfs_find_path
from reachable import reachable_tiles

import sys

def parse_output(R):

    score = int(input())

    out_grid = []
    for element in range(R):
        row = list(input())
        out_grid.append(row)

    return score, out_grid


def get_walls(grid):
    walls = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'W':
                walls.add((i, j))
    
    return walls


def validate_walls(tiles, output, wall_budget):
    R, C = len(tiles), len(tiles[0])
    count = 0

    for i in range(R):
        for j in range(C):
            if output[i][j] == 'W':
                count += 1

                if tiles[i][j] in ['#', 'a', 'b', 'c', 'p']:
                    return False, "Wall placed on illegal tile"
                
    if count > wall_budget:
        return False, "Exceeded wall budget"


    return True, "OK"


def compute_score(grid, reachable):
    score = 0
    for r, c in reachable:
        score += tile_score(grid[r][c])
    return score


if __name__ == "__main__":

    # wall_budget, R, C, tiles, horse_pos , preplaced_walls, portals = parse_input()

    # score, output = parse_output(R)

    with open(sys.argv[1]) as f:
        sys.stdin = f
        wall_budget, R, C, tiles, horse_pos , preplaced_walls, portals = parse_input()

    with open(sys.argv[2]) as f:
        sys.stdin = f
        score, output = parse_output(R)

    check, msg = validate_walls(tiles, output, wall_budget)

    if not check:
        print("INVALID", msg)
        sys.exit(0)

    walls = get_walls(output)

    path = bfs_find_path(R, C, output, walls, portals, horse_pos, preplaced_walls)

    if path is not None:
        print("INVALID: Horse can escape")
        sys.exit(0)

    reachable = reachable_tiles(R, C, output, walls, portals, horse_pos, preplaced_walls)
    actual_score = compute_score(output, reachable)

    if actual_score != score:
        print("INVALID: Score mismatch")
        print("Expected:", actual_score, "Got:", score)
    else:
        print("VALID")
