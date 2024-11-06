def multiples_of_three(a):
    while a % 3 != 0:
        a += 1

    while True:
        yield a
        a += 3


def main():
    gen = multiples_of_three(-100)
    print([next(gen) for _ in range(20)])


if __name__ == "__main__":
    main()
