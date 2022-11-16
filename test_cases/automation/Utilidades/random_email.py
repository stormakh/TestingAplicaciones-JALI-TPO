import random
import string


def random_email():
    """Generate a random email address"""
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    return '{}@{}'.format(random_string(), random.choice(domains))


def random_string():
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(random.randint(1, 16)))
