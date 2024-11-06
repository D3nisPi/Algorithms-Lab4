import random

def random_notes_generator():
    notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    for _ in range(1_000_000):
        yield random.choice(notes)


def main():
    gen = random_notes_generator()
    print([next(gen) for _ in range(20)])


if __name__ == "__main__":
    main()
