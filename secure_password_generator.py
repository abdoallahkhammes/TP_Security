import secrets
import string


def generate_secure_password(length=16, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# CSPRNG is implicitly used via secrets module (OS urandom)
if __name__ == "__main__":
    print(generate_secure_password(20))