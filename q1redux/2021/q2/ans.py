import numpy as np
from functools import lru_cache
MAXSIZE = 500

grid = np.zeros(shape=(MAXSIZE*2+1, MAXSIZE*2+1))
triangles = {}
grid[MAXSIZE][MAXSIZE] = -1

"""                  1
     / \          \-----/
 1  /   \  2   3   \   /  2     Side numbers
   /_____\          \ /
      3
"""


# Check the three 'larger triangles' around the cell at a certain row and column
def score(row, column, player_num):
    def match(r, c):
        return grid[r][c] == player_num
    # Notice that in odd index rows, odd columns are facing up and on even rows, even columns are facing up.
    if row%2==column%2:  # Facing up
        return int(match(row-1, column+1) and match(row, column+2)) + \
               int(match(row-1, column-1) and match(row, column-2)) + \
               int(match(row+1, column-1) and match(row+1, column+1))

    else:  # Facing down
        return int(match(row+1, column-1) and match(row, column-2)) + \
               int(match(row+1, column+1) and match(row, column+2)) + \
               int(match(row-1, column-1) and match(row-1, column+1))


# dRow, dColumn, new side
up = {
    1: [
        (-1, -1, 3),
        (-1, 0, 3),
        (-1, 1, 1),
        (0, 1, 1),
        (0, 0, 2)
    ],

    2: [
        (0, 2, 1),
        (1, 2, 1),
        (1, 1, 2),
        (1, 0, 2),
        (0, 0, 3)
    ],

    3: [
        (1, -1, 2),
        (1, -2, 2),
        (0, -2, 3),
        (0, -1, 3),
        (0, 0, 1)
    ]
}

# We check almost exactly the same triangles as above.
# So we can copy some bits from above, but this is still q2. It is going to be a bit tedious!
down = {
    1: [
        (-1, 1, 3),
        (-1, 2, 1),
        (0, 2, 1),
        (0, 1, 2),
        (0, 0, 2)
    ],

    2: [
        (1, 1, 1),
        (1, 0, 2),
        (1, -1, 2),
        (0, -1, 3),
        (0, 0, 3)
    ],

    3: [
        (0, -2, 2),
        (-1, -2, 3),
        (-1, -1, 3),
        (-1, 0, 1),
        (0, 0, 1)
    ]
}


between_up = {
    1: (0, -1),
    2: (0, 1),
    3: (1, 0)
}

between_down = {
    1: (-1, 0),
    2: (0, 1),
    3: (0, -1)
}

# Store the top left triangle and starting point globally.
topleft = (500, 500)
topside = 1


@lru_cache(maxsize=None)
def adjacent(row, column, side):
    if row%2 == column%2:
        dRow, dCol = between_up[side]
    else:
        dRow, dCol = between_down[side]
    return row + dRow, column + dCol


class Player:
    def __init__(self, num, traversals_per_move):
        self.row = self.column = MAXSIZE
        self.side = 1
        self.num = num
        self.traversals = traversals_per_move
        self.points = 0

    def traverse(self):
        for i in range(5):
            if self.row % 2 == self.column % 2:
                dRow, dColumn, new = up[self.side][i]
            else:
                dRow, dColumn, new = down[self.side][i]

            if grid[self.row + dRow][self.column + dColumn]:
                self.row += dRow
                self.column += dColumn
                self.side = new
                break

    def move(self):
        global topleft, topside
        # Debugging is especially essential for q2.
        # print(f"Player {self.num}")
        # Store the position of the triangle adjacent to the player.
        start_row, start_col = adjacent(self.row, self.column, self.side)
        print([self.column-500,self.row-500],[start_col-500,start_row-500])
        for i in range(self.traversals):
            self.traverse()
            temp_row, temp_col = adjacent(self.row, self.column, self.side)
            print("     ",[self.column-500,self.row-500],[temp_col-500,temp_row-500])
            if score(temp_row, temp_col, self.num):
                print("COMPLETES TRI", 500-temp_col,temp_row-500,self.num)
                break
        
        # Fill in the start point, and check whether that new triangle is the top left one.
        grid[start_row][start_col] = self.num
        triangles[(start_col-500,500-start_row)] = 1
        print(triangles)
        
        if start_row < topleft[0] or start_row == topleft[0] and start_col < topleft[1]:
            topleft = (start_row, start_col)
            topside = 1 if start_row%2==start_col%2 else 3

        # Check if the player gets any points this turn.
        self.points += score(start_row, start_col, self.num)
        # print(self.row, self.column, self.side)
        # print("\n".join(str(x[496:505]).replace(" ", "") for x in grid[496:505]))
        # print("\n")

    def reposition(self):
        adjRow, adjCol = adjacent(self.row, self.column, self.side)

        if grid[adjRow][adjCol]:
            print("REPOSITIONED!")
            self.row, self.column = topleft
            self.side = topside


def find_perimeter():
    temp = Player(-1, 0)
    temp.row, temp.column = topleft
    temp.side = topside
    perimeter = 0
    while True:
        temp.traverse()
        perimeter += 1
        if (temp.row, temp.column) == topleft and temp.side == topside:
            print(perimeter)
            break


def solve():
    p, moves = (int(x) for x in input().split())
    players = []
    traversals = [int(x) for x in input().split()]
    for i in range(p):
        players.append(Player(i+1, traversals[i]))

    while moves != 0:
        for i in range(p):
            players[i].move()
            for j in range(p):
                players[j].reposition()
            moves -= 1
            if moves == 0:
                break
        # print(players[0].row-500,players[0].column-500,players[0].side)

    for i in range(p):
        print(players[i].points)

    find_perimeter()


def b():
    # Just do this by hand! Free marks :)
    return


def c():
    global grid, topleft, topside, MAXSIZE
    MAXSIZE = 6

    def reset():
        global grid, topleft, topside
        grid = np.zeros(shape=(MAXSIZE * 2 + 1, MAXSIZE * 2 + 1))

        grid[MAXSIZE][MAXSIZE] = -1
        topleft = (MAXSIZE, MAXSIZE)
        topside = 1
    m = 4
    wanted = np.zeros(shape=(MAXSIZE * 2 + 1, MAXSIZE * 2 + 1))
    wanted[MAXSIZE][MAXSIZE] = -1
    wanted[MAXSIZE][MAXSIZE-2] = 1
    wanted[MAXSIZE][MAXSIZE-1] = 1
    wanted[MAXSIZE+1][MAXSIZE-2] = 1
    wanted[MAXSIZE+1][MAXSIZE] = 1

    # Realistically, we only need to check between 1 and 100 (the scope of the original problem)
    for i in range(1, 101):
        reset()
        player = Player(1, i)
        for _ in range(m):
            player.move()
            player.reposition()

        # See if the grid we created is the exact same as the grid we wanted.
        finished = True
        for j in range(MAXSIZE*2+1):
            for k in range(MAXSIZE*2+1):
                if grid[j][k] != wanted[j][k]:
                    finished = False
        if finished:
            print(i)  # 51


def d():
    # Solve with 2 5000\n 5 7   to fill the grid initially.
    unfilled = 0
    seen = set()
    from collections import deque
    queue = deque()

    # Fill in the triangles outside the perimeter.
    def fill(row, column):
        queue.append((row, column))

        while queue:
            r, c = queue.popleft()
            grid[r][c] = -1
            up = r%2==c%2
            if r:
                if not up and (r-1, c) not in seen and not grid[r-1, c]:
                    seen.add((r-1, c))
                    queue.append((r-1, c))
            if c:
                if (r, c-1) not in seen and not grid[r, c-1]:
                    seen.add((r, c-1))
                    queue.append((r, c-1))
            if r < 1000:
                if up and (r+1, c) not in seen and not grid[r+1, c]:
                    seen.add((r+1, c))
                    queue.append((r+1, c))
            if c < 1000:
                if (r, c+1) not in seen and not grid[r, c+1]:
                    seen.add((r, c+1))
                    queue.append((r, c+1))

    fill(0, 0)
    # Find the triangles still not filled.
    for i in range(1001):
        for j in range(1001):
            if not grid[i][j]:
                unfilled += 1
    print(unfilled)  # 377


if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    solve()
    # c()
    # d()