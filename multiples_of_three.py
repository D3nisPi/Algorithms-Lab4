def multiples_of_three(a, b):
    while a % 3 != 0:
        a += 1

    while a <= b:
        yield a
        a += 3


def main():
    START = -100
    END = 0
    MULTIPLES = 20
    gen = multiples_of_three(START, END)
    print([next(gen) for i in range(MULTIPLES)])


if __name__ == "__main__":
    main()
