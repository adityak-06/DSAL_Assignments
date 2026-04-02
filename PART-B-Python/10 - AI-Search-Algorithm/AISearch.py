from collections import deque
import heapq

# Directions: Right, Left, Down, Up
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

# Print maze with path
def print_maze(maze, path):
    maze_copy = [row[:] for row in maze]

    for (x, y) in path:
        if maze_copy[x][y] not in ('S', 'G'):
            maze_copy[x][y] = '*'

    print("\nMaze with Path:\n")
    for row in maze_copy:
        print(' '.join(row))
    print()


# ---------------- BFS ----------------
def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(maze) and 
                0 <= ny < len(maze[0]) and 
                maze[nx][ny] != '#' and 
                (nx, ny) not in visited):

                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None


# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ---------------- A* ----------------
def astar(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start))

    parent = {}
    g_score = {start: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy

            if (0 <= nx < len(maze) and 
                0 <= ny < len(maze[0]) and 
                maze[nx][ny] != '#'):

                neighbor = (nx, ny)
                tentative_g = g + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f, tentative_g, neighbor))
                    parent[neighbor] = current

    return None


# ---------------- MAIN ----------------
def main():
    print("Maze Navigation System (BFS & A*)")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nEnter maze row by row (no spaces)")
    print("S = Start, G = Goal, # = Wall, . = Free path\n")

    maze = []
    start = goal = None

    for i in range(rows):
        row = list(input(f"Row {i}: ").strip())

        if len(row) != cols:
            print("Invalid row length!")
            return

        maze.append(row)

        for j in range(cols):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'G':
                goal = (i, j)

    if start is None or goal is None:
        print("Error: Maze must contain S and G")
        return

    while True:
        print("\nMenu:")
        print("1. Solve using BFS")
        print("2. Solve using A*")
        print("3. Modify Maze")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            path = bfs(maze, start, goal)
            if path:
                print_maze(maze, path)
            else:
                print("No path found using BFS")

        elif choice == '2':
            path = astar(maze, start, goal)
            if path:
                print_maze(maze, path)
            else:
                print("No path found using A*")

        elif choice == '3':
            try:
                r = int(input("Enter row index: "))
                c = int(input("Enter col index: "))
                val = input("Enter (# or .): ").strip()

                if maze[r][c] not in ('S', 'G'):
                    maze[r][c] = val
                else:
                    print("Cannot modify Start/Goal")

                print_maze(maze, [])
            except:
                print("Invalid input!")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()