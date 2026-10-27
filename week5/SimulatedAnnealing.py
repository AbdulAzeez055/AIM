import random
import math

def calculate_cost(state):
    """
    Calculates the number of attacking pairs of queens (rows and diagonals).
    Goal is to reach a cost of 0.
    """
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                attacks += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_random_neighbor(state):
    """
    Generates a neighbor by randomly selecting one queen 
    and moving it to a different random row.
    """
    neighbor = list(state)
    n = len(state)
    
    # Pick a random column
    col = random.randint(0, n - 1)
    
    # Pick a new random row different from the current row
    current_row = state[col]
    available_rows = [r for r in range(n) if r != current_row]
    new_row = random.choice(available_rows)
    
    neighbor[col] = new_row
    return neighbor

def simulated_annealing_8_queens(initial_state, initial_temp=100.0, cooling_rate=0.995, min_temp=0.001):
    """
    Executes Simulated Annealing to solve the 8-Queens problem.
    Tracks and prints temperature cooldown states.
    """
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    T = initial_temp
    
    print("--- Start Simulated Annealing ---")
    print(f"Initial State: {current_state} | Cost: {current_cost}\n")
    
    iteration = 0
    # Loop while temperature is above the absolute minimum threshold
    while T > min_temp:
        # Check if we accidentally hit a goal state early
        if current_cost == 0:
            break
            
        # 1. Pick a random neighbor
        next_state = get_random_neighbor(current_state)
        next_cost = calculate_cost(next_state)
        
        # 2. Calculate Delta E (current.cost - next.cost)
        delta_E = current_cost - next_cost
        
        # 3. Acceptance evaluation
        if delta_E > 0:
            # Better state found, accept automatically
            current_state = next_state
            current_cost = next_cost
        else:
            # Worse state found, accept probabilistically
            probability = math.exp(delta_E / T)
            if random.random() < probability:
                current_state = next_state
                current_cost = next_cost
                
        # 4. Decrease Temperature (Geometric Cooling Schedule)
        T *= cooling_rate
        iteration += 1
        
        # Optional logging printout to trace progress every 200 iterations
        if iteration % 200 == 0:
            print(f"Iteration {iteration:4d} | Temp: {T:.4f} | Current Cost: {current_cost}")
            
    print(f"\nOptimization Finished after {iteration} steps.")
    return current_state, current_cost

# Generate a random initial layout for an 8x8 chessboard
random.seed(42)  # Fixed seed for reproducibility
initial_board = [random.randint(0, 7) for _ in range(8)]

# Execute search
final_board, final_cost = simulated_annealing_8_queens(initial_board)

print(f"Final State Config: {final_board}")
print(f"Final State Cost  : {final_cost} (Attacking pairs)")
