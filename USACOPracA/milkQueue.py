from itertools import combinations

def count_even_assignments(variables):
    counts = {
        'O': {'even': 0, 'odd': 0},
        'M': {'even': 0, 'odd': 0},
        'S': {'even': 0, 'odd': 0},
        'I': {'even': 0, 'odd': 0},
        'B': {'even': 0, 'odd': 0},
        'E': {'even': 0, 'odd': 0},
        'G': {'even': 0, 'odd': 0}
    }

    for var, val in variables:
        counts[var]['odd' if val % 2 == 1 else 'even'] += 1

    total_count = 1

    # Multiply counts of even and odd numbers
    for var_count in counts.values():
        total_count *= var_count['even'] + var_count['odd']

    return total_count

# Reading input
N = int(input())
variables = []
for _ in range(N):
    var, val = input().split()
    variables.append((var, int(val)))

# Counting even assignments
result = count_even_assignments(variables)
print(result)
