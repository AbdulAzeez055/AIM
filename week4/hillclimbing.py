import itertools

def calculate_cost(state):
    """
    Calculates the number of attacking pairs of queens.
    Checks rows and diagonals since columns are guaranteed to be unique.
    """
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check row conflict
            if state[i] == state[j]:
                attacks += 1
            # Check diagonal conflict
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(state):
    """
    Generates all unique swap neighbors and picks the best one.
    Implements the precise lexicographical tie-breaking rule.
    """
    n = len(state)
    best_neighbor = None
    min_cost = float('inf')
    best_swap_indices = (float('inf'), float('inf'))
    
    # Generate all pairs of column indices to swap
    # itertools.combinations guarantees pairs are generated in strict lexicographical order:
    # (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
    for i, j in itertools.combinations(range(n), 2):
        # Create a copy and swap the row positions
        neighbor = list(state)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        
        cost = calculate_cost(neighbor)
        
        # If it's a strictly lower cost, or a tie with a better column pair ordering
        if cost < min_cost:
            min_cost = cost
            best_neighbor = neighbor
            best_swap_indices = (i, j)
        elif cost == min_cost:
            # Tie-breaking logic: select the pair with the lower column indices
            if (i, j) < best_swap_indices:
                best_neighbor = neighbor
                best_swap_indices = (i, j)
                
    return best_neighbor, min_cost, best_swap_indices

def hill_climbing_n_queens(initial_state):
    """
    Executes the hill climbing search algorithm on the N-Queens board.
    Logs step-by-step cost evaluations for the observation book.
    """
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    
    print("--- Start Hill Climbing Optimization ---")
    print(f"Initial State: {current_state} | Initial Cost: {current_cost}\n")
    
    step = 1
    while True:
        neighbor, neighbor_cost, swapped_cols = get_best_neighbor(current_state)
        
        print(f"Step {step}:")
        print(f"  Current State : {current_state} (Cost: {current_cost})")
        print(f"  Best Neighbor : {neighbor} (Cost: {neighbor_cost}) via swapping columns {swapped_cols}")
        
        # If the best neighbor cannot improve upon the current state's cost, terminate
        if neighbor_cost >= current_cost:
            print("\nTermination: No neighbor has a lower cost. Local minimum reached.")
            break
            
        current_state = neighbor
        current_cost = neighbor_cost
        step += 1
        
        # Check if the goal state is achieved
        if current_cost == 0:
            print("\nGoal state reached! Global minimum found.")
            break
            
    return current_state, current_cost

# Define the initial state from your manual instructions: x0=3, x1=1, x2=2, x3=0
initial_configuration = [3, 1, 2, 0]
final_state, final_cost = hill_climbing_n_queens(initial_configuration)

print(f"\nFinal Board Configuration: {final_state}")
print(f"Final Attacking Pairs Cost : {final_cost}")
