def tile_score(ch):
    if ch in ['.', 'H', 'p']:
        return 1
    if ch == 'a':
        return 11
    if ch == 'b':
        return -4
    if ch == 'c':
        return 4
    return 0