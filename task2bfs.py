from collections import deque

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid_state(state):
    missionaries_left, cannibals_left, _ = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if (missionaries_left != 0 and missionaries_left < cannibals_left) or (missionaries_right != 0 and missionaries_right < cannibals_right):
        return False
    return True

def get_next_states(state):
    states = []
    missionaries_left, cannibals_left, boat_position = state

    if boat_position == 1:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left - m, cannibals_left - c, 0)
                    if is_valid_state(new_state):
                        states.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries_left + m, cannibals_left + c, 1)
                    if is_valid_state(new_state):
                        states.append(new_state)
    return states

def bfs():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        if current_state not in visited:
            visited.add(current_state)
            for next_state in get_next_states(current_state):
                queue.append((next_state, path + [current_state]))
    return None

def print_solution(solution):
    print("Missionaries and Cannibals Solution:")
    for state in solution:
        missionaries_left, cannibals_left, boat_position = state
        missionaries_right = 3 - missionaries_left
        cannibals_right = 3 - cannibals_left
        print(f"Start Side: {missionaries_left}M {cannibals_left}C  End side: {missionaries_right}M {cannibals_right}C  Boat: {'Left' if boat_position == 1 else 'Right'}")

solution = bfs()

if solution:
    print_solution(solution)
else:
    print("No solution found.")