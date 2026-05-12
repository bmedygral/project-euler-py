def multiples_of_n(n: int, upper_limit: int):
    m = 1
    while n * m < upper_limit:
        yield n * m
        m += 1


def sum_of_multiples_of_ns(ns: list[int], upper_limit: int) -> int:
    multiples = {multiple for n in ns for multiple in multiples_of_n(n, upper_limit)}
    return sum(multiples)


if __name__ == "__main__":
    result = sum_of_multiples_of_ns([3, 5], 1000)
    print(result)
