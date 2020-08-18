
def get_fibonacci_number(n: int):
    validate(n)
    if n <= 2:
        nth_fibonacci = n
    else:
        nth_fibonacci = get_fibbonacci_number_for_n_grater_than_2(n)
    return nth_fibonacci


def get_fibbonacci_number_for_n_grater_than_2(n: int):
        previous_second = 1
        previous_first = 2
        nth_fibonacci = None
        for _ in range(3, n+1):
            nth_fibonacci = previous_second + previous_first
            previous_second = previous_first
            previous_first = nth_fibonacci
        return nth_fibonacci


def sum_of_even_valued_fibonacci_numbers(upper_limit: int):
    sum = 0
    n = 1
    fib_number = get_fibonacci_number(n = 1)
    while fib_number <= upper_limit:
        fib_number = get_fibonacci_number(n)
        if fib_number % 2 == 0:
            sum += get_fibonacci_number(n)
        n += 1
    return sum


def validate(n):
    if n < 1:
        raise ValueError("n must be >= 1")


if __name__ == '__main__':
    print(sum_of_even_valued_fibonacci_numbers(4_000_000))
