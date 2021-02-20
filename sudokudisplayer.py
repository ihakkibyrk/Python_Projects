def sudoku_displayer(arg):
    count = 0
    line = 0
    for i in arg:
        i.insert(3,"|")
        i.insert(7, "|")
    while count < len(arg) + 4 and line < len(arg):
        
        if count % 3 == 0:
            print(*("-"*(len(arg) + 2)))
            print(*arg[line])
        elif count % 3 == 1:
            print(*arg[line])
        elif count % 3 == 2 and line == len(arg) -1:
            print(*arg[line])
            print(*("-"*(len(arg) + 2)))
        else:
            print(*arg[line])
            
                
        line += 1
           
        count += 1



sudoku_displayer([
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
])