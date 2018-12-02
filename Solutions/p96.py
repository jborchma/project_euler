"""Solution to problem 96

My solutions is pretty straight forward. Mainly, it applies rules for each row, column and cell
for a given grid and stores
"""

from copy import deepcopy

N = 9
CELL_SIZE = 3

def load_grids():
    """Function to load grids into memory
    """
    list_of_grids = []
    index_counter = -1
    with open('p096_sudoku.txt', 'r') as file:
        for i, line in enumerate(file):
            if i % 10 == 0:
                index_counter += 1
                list_of_grids.append([])
            else:
                list_of_grids[index_counter].append([int(digit) for digit in str.strip(line)])

    return list_of_grids

def initialize_grid(grid):
    """Initializes grid. Sets in each square either the number or in case of a 0 a set of all
    9 digits.
    """
    initial_state = grid.copy()
    for i in range(N):
        for j in range(N):
            if grid[i][j] in range(1, 10):
                initial_state[i][j] = grid[i][j]
            else:
                initial_state[i][j] = set(range(1, 10))

    return initial_state

def propagate_knowledge(current_state):
    """Propagate the current knowledge and eliminate impossible numbers
    """
    #current_state = current_state.copy()
    new_values_found = 0

    # go through all cells
    for x_cell in range(N//CELL_SIZE):
        for y_cell in range(N//CELL_SIZE):
            cell_values = set()
            # fill in cell digits
            for i in range(CELL_SIZE * x_cell, CELL_SIZE * x_cell + CELL_SIZE):
                for j in range(CELL_SIZE * y_cell, CELL_SIZE * y_cell + CELL_SIZE):
                    if isinstance(current_state[i][j], int):
                        cell_values.add(current_state[i][j])
            # make inference
            for i in range(CELL_SIZE * x_cell, CELL_SIZE * x_cell + CELL_SIZE):
                for j in range(CELL_SIZE * y_cell, CELL_SIZE * y_cell + CELL_SIZE):
                    if isinstance(current_state[i][j], set):
                        current_state[i][j] -= cell_values
                        if len(current_state[i][j]) == 1:
                            new_value = current_state[i][j].pop()
                            current_state[i][j] = new_value
                            cell_values.add(new_value)
                            new_values_found += 1
                        elif len(current_state[i][j]) == 0:
                            return current_state, False, None

    # go through all rows
    for i in range(N):
        row = current_state[i]
        row_values = set(digit for digit in row if isinstance(digit, int))
        for j in range(N):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= row_values
                if len(current_state[i][j]) == 1:
                    new_value = current_state[i][j].pop()
                    current_state[i][j] = new_value
                    row_values.add(new_value)
                    new_values_found += 1
                elif len(current_state[i][j]) == 0:
                    return current_state, False, None

    # go through all columns
    for j in range(N):
        column = [current_state[i][j] for i in range(N)]
        column_values = set(digit for digit in column if isinstance(digit, int))
        for i in range(N):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= column_values
                if len(current_state[i][j]) == 1:
                    new_value = current_state[i][j].pop()
                    current_state[i][j] = new_value
                    column_values.add(new_value)
                    new_values_found += 1
                elif len(current_state[i][j]) == 0:
                    return current_state, False, None

    return current_state, True, new_values_found

def propagate(grid):
    """Propagate our knowledge until we can't find any more numbers by just
    applying the rules.
    """
    while True:
        current_state, solvable, new_values_found = propagate_knowledge(grid)
        if not solvable:
            return current_state, False
        if new_values_found == 0 or new_values_found is None:
            return current_state, True

def guess(current_state):
    """Solve the sudoku puzzle

    First, we apply the rules and eliminate as many possiblities as possible. Once we have
    exhausted all the rule applications, we start guessing for each undetermined cell out of
    all the possiblities. Once we have arrived at the correct solution, we are done.
    """
    current_state, solvable = propagate(current_state)

    if not solvable:
        return None

    if done(current_state):
        return current_state

    for i in range(N):
        for j in range(N):
            if isinstance(current_state[i][j], set):
                for value in current_state[i][j]:
                    new_state = deepcopy(current_state)
                    new_state[i][j] = value
                    solved = guess(new_state)
                    if solved is not None:
                        return solved
                return None


def extract_digit(grid):
    """Solves a sudou puzzle and extracts the top three digits
    """
    initial_state = initialize_grid(grid)
    solved_state = guess(initial_state)

    #print(solved_state)
    digits = ''
    for digit in solved_state[0][:3]:
        digits += str(digit)

    return int(digits)

def done(grid):
    """Check if grid is solved.

    In case all digits are determined, test if the grid is consistent.
    """
    for row in grid:
        for cell in row:
            if isinstance(cell, set):
                return False

    for row in grid:
        if sum(row) != 45:
            return False

    for j in range(N):
        if sum([grid[i][j] for i in range(N)]) != 45:
            return False

    return True

def main():
    """main function
    """
    sum_of_digits = 0
    list_of_all_grids = load_grids()
    for grid in list_of_all_grids:
        digits = extract_digit(grid)
        print(digits)
        sum_of_digits += digits

    print(sum_of_digits)

if __name__ == "__main__":
    main()
