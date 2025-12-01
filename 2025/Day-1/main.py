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



with open("input.txt") as f:
    lines = f.readlines()

ans = solution(lines)
print(ans)
