from collections.abc import Iterator


def fibb(n: int) -> Iterator[int]:
    v1 = 1
    yield v1

    v2 = 2
    while v2 <= n:
        yield v2

        v2_new = v1 + v2
        v1 = v2
        v2 = v2_new

def sum_of_even_fibb(up_to: int) -> int:
    return sum(f for f in fibb(up_to) if f % 2 == 0)

if __name__=="__main__":
    print(sum_of_even_fibb(sum_of_even_fibb(4*10**6)))
