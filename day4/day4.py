class Day4:
    def parseInput(self):
        grid = []
        with open("input.txt", "r") as file:
            for line in file:
                grid.append(list(line.strip()))
        print(grid)
        return grid

    def part1(self):
        grid = self.parseInput()
        ROWS = len(grid)
        COLS = len(grid[0])
        answer = 0

        directions = [
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1,-1]
        ]

        for i in range(ROWS):
            for j in range(COLS):
                num_paper = 0
                if grid[i][j] == "@":
                    for (x, y) in directions:
                        idx_x, idx_y = i + x, j + y
                        if 0 <= idx_x < ROWS and 0 <= idx_y < COLS:
                            if grid[idx_x][idx_y] == "@":
                                num_paper += 1
                    if num_paper < 4:
                        answer += 1

        return answer




if __name__ == "__main__":
    day4 = Day4()
    print(day4.parseInput())
    print(day4.part1())
