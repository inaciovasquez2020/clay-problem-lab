def simulate(n):
    H = n
    steps = 0
    while H > 0:
        H -= 1
        steps += 1
    return steps

print(simulate(100))
