from collections import deque

def reachable_tiles(R, C, grid, walls, portals, horse_pos, preplaced_walls):
    visited = set([horse_pos])
    queue = deque([horse_pos])

    while queue:
        r, c = queue.popleft()

        # portal jump
        if (r, c) in portals:
            pr, pc = portals[(r, c)]
            if (pr, pc) not in visited:
                visited.add((pr, pc))
                queue.append((pr, pc))

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                if (nr, nc) not in visited and (nr, nc) not in walls:
                    nt = grid[nr][nc]
                    if nt != '#' and (nt != 'W' or (nr, nc) in preplaced_walls):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    return visited
