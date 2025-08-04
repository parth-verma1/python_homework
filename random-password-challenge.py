import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pwd = ''.join(random.sample(chars, 8))
print("ur password is:", pwd)
