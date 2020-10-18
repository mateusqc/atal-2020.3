#URI - 1905
n = int(input())

def is_valid_neighbour(position):
    if (position[0] >= 0 and position[1] >= 0) and (position[0] <= 4 and position[1] <= 4):
        return True
    return False

def find_valid_neighbours(matrix, visited, position):
    add_tuples = [(1,0), (0,1), (-1, 0), (0, -1)]
    neighbours = []
    for add_tuple in add_tuples:
        new_position = (position[0] + add_tuple[0], position[1] + add_tuple[1])
        if is_valid_neighbour(new_position) and visited[new_position[0]][new_position[1]] == 0 and matrix[new_position[0]][new_position[1]] == '0':
            neighbours.append(new_position)
    return neighbours

def find_path(matrix, visited, position):
    visited[position[0]][position[1]] = 1
    if position[0] == 4 and position[1] == 4:
        return True    
    else:
        result = False
        neighbours = find_valid_neighbours(matrix, visited, position)
        for neighbour in neighbours:
            result = result or find_path(matrix, visited, neighbour)
        return result


for rep in range(n):
    matrix = []
    visited = []
    count = 0
    while count < 5:
        line = input().split()
        if len(line) < 5:
            continue
        else:
            matrix.append(line)
            visited_line = []
            for j in range(5):
                visited_line.append(0)
            visited.append(visited_line)
            count += 1

    result = find_path(matrix, visited, (0,0))

    if result:
        print('COPS')
    else:
        print('ROBBERS')