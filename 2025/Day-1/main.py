'''
    1. Start dial position pos = 50
    2. read diretions (L or R)
        L :- pos -= dis
        R :- pos += dis

        circular rotation pos = pos%100
    3. after each rotation check if pos = 0
    4. after processing each things teh final result is the password

'''
def solution(lines):
    pos = 50
    count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        dir = line[0]
        dist = int(line[1:])
        if dir == "L":
            pos = (pos - dist) % 100
        elif dir == "R":
            pos = (pos + dist) % 100

        if pos == 0:
            count += 1
    return count

def count_zero_hits(lines):
    pos = 50
    zeros = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        dir_char = line[0].upper()
        steps = int(line[1:])
        if dir_char == 'L':
            pos = (pos - steps) % 100
        elif dir_char == 'R':
            pos = (pos + steps) % 100
        else:
            raise ValueError(f"Unknown direction: {dir_char}")
        if pos == 0:
            zeros += 1
    return zeros

with open("input.txt") as f:
    lines = f.readlines()

answer = count_zero_hits(lines)
ans = solution(lines)
print(ans)
print(answer)
