import string
import secrets


def product_url():
    alphabet = string.ascii_lowercase
    random_letters = "".join(secrets.choice(alphabet) for _ in range(6))
    return random_letters
