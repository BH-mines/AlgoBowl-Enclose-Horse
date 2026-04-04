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

    P = int(input()) # Prase the portals
    portals = {}
    for _ in range(P):
        r1, c1, r2, c2 = map(int, input().split())
        portals[(r1, c1)] = (r2, c2)
        portals[(r2, c2)] = (r1, c1)

    return wall_budget, R, C, tiles, horse_pos, preplaced_walls, portals
### Testing the parse
if __name__ == "__main__":
    wall_budget, R, C, tiles, horse_pos, preplaced_walls, portals = parse_input()
    print(f"Wall budget: {wall_budget}")
    print(f"Dimensions: {R} rows x {C} cols")
    print(f"Horse position: {horse_pos}")
    print(f"Preplaced walls: {preplaced_walls}")
    print(f"Portals:{portals}")