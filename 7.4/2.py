#URI - 1556
while True:
    solutions = set([])
    try:
        full_string = str(input())
    except EOFError:
        break

    for letter in full_string:
        for solution in solutions.copy():
            solutions.add(solution + letter)
        solutions.add(letter)

    for element in sorted(solutions):
        print(element)
    print('')
