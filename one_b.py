def basement(instructions):
    floors = 0
    for i in range(len(instructions)):
        if instructions[i] == '(':
            floors += 1
        elif instructions[i] == ')':
            floors -= 1
        if floors == -1:
            return i+1
