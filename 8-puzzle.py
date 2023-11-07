import heapq

# Define the size of the puzzle (3x3)
PUZZLE_SIZE = 3

# Define the possible moves (up, down, left, right) along with their corresponding directions
MOVES = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(PUZZLE_SIZE):
        for j in range(PUZZLE_SIZE):
            if state[i][j] != 0:
                target_x, target_y = divmod(goal_state[i][j] - 1, PUZZLE_SIZE)
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Function to check if a state is valid
def is_valid(x, y):
    return 0 <= x < PUZZLE_SIZE and 0 <= y < PUZZLE_SIZE

# Function to perform A* search to solve the puzzle and record the path
def solve_puzzle(start_state, goal_state):
    open_set = [(manhattan_distance(start_state, goal_state), start_state, '', 0)]
    visited = set()
    came_from = {}  # Dictionary to store the parent state for each state
    move_counter = 0  # Move counter

    while open_set:
        _, current_state, direction, _ = heapq.heappop(open_set)

        if tuple(map(tuple, current_state)) == tuple(map(tuple, goal_state)):
            # Backtrack from goal state to start state to construct the path
            path = [(current_state, direction, move_counter)]
            while tuple(map(tuple, current_state)) != tuple(map(tuple, start_state)):
                current_state, direction = came_from[tuple(map(tuple, current_state))]
                path.append((current_state, direction, move_counter))
            path.reverse()  # Reverse the path to get the correct order
            return path

        visited.add(tuple(map(tuple, current_state)))
        x, y = None, None

        # Find the position of the empty tile
        for i in range(PUZZLE_SIZE):
            for j in range(PUZZLE_SIZE):
                if current_state[i][j] == 0:
                    x, y = i, j

        for dx, dy, new_direction in MOVES:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = [list(row) for row in current_state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                if tuple(map(tuple, new_state)) not in visited:
                    priority = manhattan_distance(new_state, goal_state)
                    heapq.heappush(open_set, (priority, new_state, new_direction, 0))
                    # Store the parent state and direction for the current state
                    came_from[tuple(map(tuple, new_state))] = (current_state, new_direction)
                    move_counter += 1

    return None

if __name__ == "__main__":
    print("Enter the starting state of the 8-puzzle:")
    start_state = []
    for _ in range(PUZZLE_SIZE):
        row = list(map(int, input().split()))
        start_state.append(row)

    print("Enter the goal state of the 8-puzzle:")
    goal_state = []
    for _ in range(PUZZLE_SIZE):
        row = list(map(int, input().split()))
        goal_state.append(row)

    solution_path = solve_puzzle(start_state, goal_state)

    if solution_path:
        print("\nSolution found! Path to reach the goal state:")
        for move_number, (state, direction, _) in enumerate(solution_path):
            print("Move number:", move_number)
            print("Direction:", direction)
            for row in state:
                print(" ".join(map(str, row)))
        print("Goal state reached")
    else:
        print("\nNo solution found.")