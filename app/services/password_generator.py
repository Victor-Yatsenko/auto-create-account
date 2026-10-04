from app.core.config import Config

import random

# Щоб не плутати юзера, прибрані I O o l 0
upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
lower = "abcdefghijkmnpqrstuvwxyz"
number = "123456789"
symbols = "-!"

def password_generator():
    password = []
    for p in range(Config.LEN_PASS):
        password.append(random.choice(upper))
        password.append(random.choice(lower))
        password.append(random.choice(number))
        password.append(random.choice(symbols))

    random.shuffle(password)
    password = "".join(password)[:Config.LEN_PASS]
    return password
