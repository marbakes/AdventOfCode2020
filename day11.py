def seatmap(file_name):
    with open(file_name, 'r') as reader:
        return  [i.strip() for i in reader.readlines()]

def neighbors(x, y, grid, visibility_mode):

    sum_neighbors = 0

    for i in range(y - 1, y + 2):
        
        for j in range (x - 1, x + 2):

            if i < 0 or j < 0:
                pass
            
            elif i >= len(grid) or j >= len(grid[i]):
                pass

            elif i == y and j == x:
                pass

            elif grid[i][j] == '#':

                sum_neighbors += 1

            elif visibility_mode and grid[i][j] == '.':

                if j == x:
                    
                    x_dir = 0
                
                else:

                    x_dir = int((j - x) / abs(j - x))

                if i == y:
                    
                    y_dir = 0
                
                else:

                    y_dir = int((i - y) / abs(i - y))

                i_prime = i
                j_prime = j

                while i_prime < len(grid) and j_prime < len(grid[i_prime]) and i_prime >= 0 and j_prime >= 0:

                    if grid[i_prime][j_prime] == 'L':
                        
                        break

                    elif grid[i_prime][j_prime] == '#':

                        sum_neighbors += 1
                        break

                    i_prime += y_dir
                    j_prime += x_dir
            

    return sum_neighbors


def seating(file_name, visibility_mode):

    grid = seatmap(file_name)

    if visibility_mode:

        n_limit = 5
    
    else:

        n_limit = 4

    while True:

        newgrid = grid.copy()

        for y in range(len(grid)):

            for x in range(len(grid[y])):

                if grid[y][x] == '.':

                    pass

                else:
                
                    if grid[y][x] == 'L' and neighbors(x, y, grid, visibility_mode) == 0:

                        newgrid[y] = newgrid[y][:x] + '#' + newgrid[y][x + 1:]

                    if grid[y][x] == '#' and neighbors(x, y, grid, visibility_mode) >= n_limit:

                        newgrid[y] = newgrid[y][:x] + 'L' + newgrid[y][x + 1:]

        if newgrid != grid:

            grid = newgrid.copy()

        else:

            return sum([row.count('#') for row in grid])

print(seating('inputs/11/test_a.txt', True))
print(seating('inputs/11/input_a.txt', True))
