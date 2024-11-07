import random

def random_notes_generator():
    ITERS = 1_000_000
    notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    for i in range(ITERS):
        yield random.choice(notes)


def main():
    NOTES = 20
    gen = random_notes_generator()
    print([next(gen) for i in range(NOTES)])


if __name__ == "__main__":
    main()
