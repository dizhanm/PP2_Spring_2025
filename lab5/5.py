import re


def a_b(text):
    return bool(re.fullmatch(r'a.*b$' , text))

print(a_b("asf1n_cb"))