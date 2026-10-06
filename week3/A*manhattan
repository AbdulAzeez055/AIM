import heapq

start = (2,8,3,1,6,4,7,0,5)
goal  = (1,2,3,8,0,4,7,6,5)

def h(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(j, 3)
            distance += abs(r1-r2) + abs(c1-c2)

    return distance

def moves(state):
    p = state.index(0)
    r, c = divmod(p, 3)

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            q = nr*3 + nc
            s = list(state)
            s[p], s[q] = s[q], s[p]
            yield tuple(s)

def astar():
    pq = [(h(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        for nxt in moves(state):
            heapq.heappush(pq, (g+1+h(nxt), g+1, nxt,
                                path + [state]))

solution = astar()

for state in solution:
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()
