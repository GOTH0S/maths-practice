import random
import numpy as np

def flip_coins(num_coins):
    heads = 0

    for _ in range(num_coins):
        if random.random() < 0.5:
            heads += 1

    return heads


n = 10
trials = 1_000_000
wins = 0

for _ in range(trials):
    a_heads = flip_coins(n + 1)
    b_heads = flip_coins(n)

    if a_heads > b_heads:
        wins += 1

p = np.round(float(wins / trials), 2)
print(f"p({p})")