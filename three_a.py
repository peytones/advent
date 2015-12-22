import numpy
def deliver(house_list):
    f = open(house_list, 'r')
    houses = f.read().strip('\n')
    visited = numpy.zeros(shape=(len(houses), len(houses)))
    row = 0
    col = 0
    count = 0
    for i in range(len(houses)):
        symbol = houses[i]
        if symbol == '>': row += 1
        elif symbol == '<': row -= 1
        elif symbol == '^': col += 1
        elif symbol == 'v': col -= 1
        house = visited[row][col]
        if house == 0:
            count += 1 
            visited[row][col] = 1
    print(count)

