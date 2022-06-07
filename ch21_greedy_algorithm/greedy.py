from typing import List, Tuple


'''
배낭 문제
'''
Cargo = List[Tuple[int, int]] 

cargo: Cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]

def fractional_knapsack(cargo: Cargo) -> float:
    capacity: int = 15
    pack: List[int] = []
    
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)
    
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    
    return total_value

result = fractional_knapsack(cargo)

print(result)
