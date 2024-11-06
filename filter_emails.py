import re

def is_valid_email(email):
    pattern = r'^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z]+$'
    return bool(re.fullmatch(pattern, email))


def main():
    emails = input("Введите email-адреса через пробел: ").split()
    valid_emails = list(filter(is_valid_email, emails))
    print(f"Корректные адреса: {valid_emails}")


if __name__ == "__main__":
    main()
