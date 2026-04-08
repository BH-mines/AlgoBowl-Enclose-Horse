from collections import deque
import sys

def parse_input():
    wall_budget = int(input()) # Grab wall budget
    R, C = map(int, input().split()) # Grab row and cols

    tiles = [] 
    horse_pos = None # keep track of horse position
    preplaced_walls = set() # keep track of the preplaced_walls using a set

    for r in range(R): # look through the rows
        row = list(input())
        for c, ch in enumerate(row):
            if ch == 'H':
                horse_pos = (r, c)
            if ch == 'W':
                preplaced_walls.add((r, c))
        tiles.append(row)

    P = int(input()) # parse the portals
    portals = {}
    for _ in range(P):
        r1, c1, r2, c2 = map(int, input().split())
        portals[(r1, c1)] = (r2, c2)
        portals[(r2, c2)] = (r1, c1)

    return wall_budget, R, C, tiles, horse_pos, preplaced_walls, portals

# Returns a path if the horse can escape, or None if its enclosed
def bfs_find_path(R, C, tiles, walls, portals, horse_pos, preplaced_walls=set()):

    parent = {horse_pos: None} # Dict tracking each tile, horse pos maps to none since it starts w/ no parent
    queue = deque([horse_pos]) # Standard BFS queue starting from the horse

    while queue:
        r, c = queue.popleft() # Pop next tile to explore from the front of queue

        # We check to see if the current tile is on the perimeter. If so then the horse can escape
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            path = []
            pos = (r, c)
            while pos is not None:
                path.append(pos)
                pos = parent[pos]
            path.reverse()
            return path

        # Traceback from the perimeter to horse using parent pointers, in reverse going from horse -> perimeter.
        if (r, c) in portals:
            partner = portals[(r, c)]
            if partner not in parent:
                parent[partner] = (r, c)
                queue.append(partner)

        # If current tile is a portal and we haven't visited the partner yet, add partner in the queue as a neighbor
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C: # check all 4 directional neighbors
                if (nr, nc) not in parent and (nr, nc) not in walls: # grid bounds!
                    nt = tiles[nr][nc] # skip if visited or blocked by a wall we placed
                    if nt != '#' and (nt != 'W' or (nr, nc) in preplaced_walls):
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))

    return None

#Algorithm to block path of horse
def place_wall(R, C, tiles, walls, wall_budget, portals, horse_pos, preplaced_walls):
    wall_count = len(preplaced_walls) #Start the wall count with only preplaced walls
    path = bfs_find_path(R, C, tiles, walls, portals, horse_pos, preplaced_walls) #store current path out
    if path != None: 
        while wall_count < wall_budget:
            index = 1 #Start at index 1 as index 0 is the horse itself
            while tiles[path[index][0]][path[index][1]] != '.':
                index += 1
                if index >= len(path):
                    return
            tiles[path[index][0]][path[index][1]] = 'W' #Place wall on first availabel in path
            wall_count += 1
            path = bfs_find_path(R, C, tiles, walls, portals, horse_pos, preplaced_walls)
            if path == None: #If path is now blocked, output new configuration and number of walls used
                return tiles, wall_count
    return None, None


if __name__ == "__main__":
    
    wall_budget, R, C, tiles, horse_pos, preplaced_walls, portals = parse_input()
    # Use existing W tiles as blocked walls for testing
    walls = set(preplaced_walls)

    bfs_run = bfs_find_path(R, C, tiles, walls, portals, horse_pos, preplaced_walls)

    print("Wall budget:", wall_budget)
    print("Horse position:", horse_pos)
    print("Preplaced walls:", preplaced_walls)
    print("Portals:", portals)
    print("Path:", bfs_run)

    newTiles, wall_count = place_wall(R, C, tiles, walls, wall_budget, portals, horse_pos, preplaced_walls)
    print("Tiles with new walls:", newTiles)
    print("Current total wall count:", wall_count)

    