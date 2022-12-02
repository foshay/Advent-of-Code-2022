
key = {
    ('A', 'X') : 4, # Draw 3 + 1 rock
    ('A', 'Y') : 8, # Win 6 + 2 paper
    ('A', 'Z') : 3, # Loss 0 + 3 scissors
    ('B', 'X') : 1, # Loss 0 + 1 rock
    ('B', 'Y') : 5, # Draw 3 + 2 paper
    ('B', 'Z') : 9, # Win 6 + 3 scissors
    ('C', 'X') : 7, # Win 6 + 1 rock
    ('C', 'Y') : 2, # Loss 0 + 2 Paper
    ('C', 'Z') : 6, # Draw 3 + 3 scissors
}

with open("input.txt","r") as fp:
    total = 0
    lines = fp.read().splitlines()
    for x in lines:
        a, b = x.split(' ')
        total += key[(a, b)]
    print(total)
