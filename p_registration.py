def sum_of_odd_squares(n: int) -> int:
    return sum(i**2 for i in range(1, n, 2))


if __name__ == "__main__":
    n = 413 * 10**3
    result = sum_of_odd_squares(n)
    print(result)
