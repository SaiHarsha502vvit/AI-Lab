def format_bank(bank):
    return f"({bank[0]} Missionaries , {bank[1]} Cannibales, {bank[2]} boat)"

def is_valid(state):
    left_bank, right_bank = state
    if (left_bank[0] < left_bank[1] and left_bank[0] > 0) or (right_bank[0] < right_bank[1] and right_bank[0] > 0):
        return False
    for value in left_bank + right_bank:
        if value < 0 or value > n:
            return False
    return True

def generate_successors(state):
    left_bank, right_bank = state  # left ((4, 4, 1),  Right (0, 0, 0))
    successors = []
    if left_bank[2] == 1:
        for m in range(n + 1):
            for c in range(n + 1):
                if m + c > 0 and m + c <= boat_capacity:  
                    new_left = (left_bank[0] - m, left_bank[1] - c, 0)
                    new_right = (right_bank[0] + m, right_bank[1] + c, 1)
                    new_state = (new_left, new_right)
                    if is_valid(new_state):
                        successors.append(new_state)
    else:
        for m in range(n + 1):
            for c in range(n + 1):
                if m + c > 0 and m + c <= boat_capacity:
                    new_left = (left_bank[0] + m, left_bank[1] + c, 1)
                    new_right = (right_bank[0] - m, right_bank[1] - c, 0)
                    new_state = (new_left, new_right)
                    if is_valid(new_state):
                        successors.append(new_state)
    return successors

def solve():
    start_state = ((n, n, 1), (0, 0, 0))
    goal_state = ((0, 0, 0), (n, n, 1))
    frontier = [([start_state], [start_state])]
    while frontier:
        path, state = frontier.pop(0)  # Path  [((4, 4, 1), (0, 0, 0))]   state  [((4, 4, 1), (0, 0, 0))]
        current_state = state[-1]  # Current State  ((4, 4, 1), (0, 0, 0))
        if current_state == goal_state:
            return path
        for successor in generate_successors(current_state):
            if successor not in state:
                new_path = list(path)
                new_path.append(successor)
                new_state = list(state)
                new_state.append(successor)
                frontier.append((new_path, new_state))
    return None

def print_solution(path):
    if path:
        for i, state in enumerate(path):
            left_bank, right_bank = state
            print(f"Step {i + 1}")
            print(f"Left Bank: {format_bank(left_bank)}")
            print(f"Right Bank: {format_bank(right_bank)}")
            print()

    
n = int(input("Enter the number of missionaries and cannibals: "))
boat_capacity = int(input("Enter the boat capacity: "))
solution_path = solve()
if solution_path:
    print("Solution Found:")
    print_solution(solution_path)
else:
    print("No solution found")

