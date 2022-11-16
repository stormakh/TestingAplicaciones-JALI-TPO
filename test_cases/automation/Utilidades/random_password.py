# create random password generator

import random
import string

# pass con digitos


def random_password(lenght):
    flag = 0
    while(flag != 1):
        # reset dict
        dict = {'upper': 0, 'lower': 0, 'digit': 0, 'punctuation': 0}
        password = ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation) for _ in range(lenght))
        for char in password:
            if char.isupper():
                dict['upper'] += 1
            elif char.islower():
                dict['lower'] += 1
            elif char.isdigit():
                dict['digit'] += 1
            elif char in string.punctuation:
                dict['punctuation'] += 1
        if dict['upper'] > 0 and dict['lower'] > 0 and dict['digit'] > 0 and dict['punctuation'] > 0:

            flag = 1
    return password


def random_password_nodigits(lenght):
    return ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(lenght))


def random_password_nopunctuation(lenght):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(lenght))


def random_password_nodigits_nopunctuation(lenght):
    return ''.join(random.choice(string.ascii_letters) for _ in range(lenght))


def random_password_nodigits_nopunctuation_nouppercase(lenght):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(lenght))


def random_password_onlydigits(lenght):
    return ''.join(random.choice(string.digits) for _ in range(lenght))


def custom_password(upper, lower, digit, punctuation):
    flag = 0
    lenght = upper + lower + digit + punctuation
    if upper == 0 and lower == 0 and digit == 0 and punctuation == 0:
        print("No se puede generar una contraseña sin ningun caracter")
        return

    while(flag != 1):
        # reset dict
        dict = {'upper': 0, 'lower': 0, 'digit': 0, 'punctuation': 0}
        password = ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation) for _ in range(lenght))
        for char in password:
            if char.isupper():
                dict['upper'] += 1
            elif char.islower():
                dict['lower'] += 1
            elif char.isdigit():
                dict['digit'] += 1
            elif char in string.punctuation:
                dict['punctuation'] += 1
        if dict['upper'] >= upper and dict['lower'] >= lower and dict['digit'] >= digit and dict['punctuation'] >= punctuation:

            flag = 1
    return password
