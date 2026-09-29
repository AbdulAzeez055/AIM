def dfs(src, target, limit, visited_states):
    if src == target:
        return True
    if limit == 0:
        return False
    visited_states.append(src)
    poss_moves_to_do = possible_moves(src, visited_states)
    for move_to in poss_moves_to_do:
        if dfs(move_to, target, limit - 1, visited_states):
            return True
    visited_states.pop()
    return False

def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    if b not in:
        d.append('u')
    if b not in:
        d.append('d')
    if b not in:
        d.append('l')
    if b not in:
        d.append('r')
    pos_moves_it_can = []         
    for i in d:
        pos_moves_it_can.append(gen(state, i, b))
    return [move_it_can for move_it_can in pos_moves_it_can if move_it_can not in visited_states]

def gen(state, m, b):
    temp = state.copy()                                       
    if m == 'd':
        temp[b + 3], temp[b] = temp[b], temp[b + 3]
    if m == 'u':
        temp[b - 3], temp[b] = temp[b], temp[b - 3]
    if m == 'l':
        temp[b - 1], temp[b] = temp[b], temp[b - 1]
    if m == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]
    return temp

def iddfs(src, target, max_depth):
    for i in range(1, max_depth + 1):
        visited_states = []
        if dfs(src, target, i, visited_states):
            return True
    return False

src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]
depth = 2
print("Test 1 Result:", iddfs(src, target, depth))

src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 6, 4, 5, -1, 7, 8]
depth = 1
print("Test 2 Result:", iddfs(src, target, depth))

src = [1, 2, 3, 4, 5, 6, 7, -1, 8]
target = [1, 2, 3, 4, 5, 6, -1, 7, 8]
for d in range(1, 30):
    if iddfs(src, target, d):
        print(f"Test 3 Target found at minimum depth: {d}")
        break

src = [1, 2, 3, 4, 5, 6, 7, 8, -1]
target = [-1, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(1, 100):
    val = iddfs(src, target, i)
    print(i, val)
    if val == True:
        break
