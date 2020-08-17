from typing import List

def sum_of_multiples_below(n: int, multipliers: List[int]):
    validate_input(n, multipliers)

    multiples_sum = 0
    for multiple_candidate in range(1, n):
        if is_multiple(multiple_candidate, multipliers):
            multiples_sum += multiple_candidate
    
    return multiples_sum


def is_multiple(candidate: int, multipliers: List[int]):
    return any(map(lambda m: candidate % m == 0, multipliers))


def validate_input(n: int, multipliers: List[int]):
    any_multiples_below_zero = any(filter(lambda m: m<0, multipliers))
    if n < 0 or any_multiples_below_zero:
        raise ValueError("n must be natural")


if __name__== '__main__':
    print(sum_of_multiples_below(n=1000, multipliers=[3, 5]))
