import functools

class Tile:

    def __init__(self, ini):
        self.tiles = [row[:] for row in ini]
        self.fn = 0
        self.gn = 0
        self.hn = 0
        self.i = 0
        self.j = 0

    def misplaced_tiles(self):
        num = 0
        mat = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        for i in range(3):
            for j in range(3):
                if mat[i][j] != self.tiles[i][j]:
                    num += 1
        return num

    def calculate_fn(self):
        self.hn = self.misplaced_tiles()
        self.fn = self.hn + self.gn

    def find_space(self):
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    self.i = i
                    self.j = j
                    return i, j

    def up(self):
        self.find_space()
        t = self.tiles[self.i][self.j]
        self.tiles[self.i][self.j] = self.tiles[self.i - 1][self.j]
        self.tiles[self.i - 1][self.j] = t

    def down(self):
        self.find_space()
        t = self.tiles[self.i][self.j]
        self.tiles[self.i][self.j] = self.tiles[self.i + 1][self.j]
        self.tiles[self.i + 1][self.j] = t

    def left(self):
        self.find_space()
        t = self.tiles[self.i][self.j]
        self.tiles[self.i][self.j] = self.tiles[self.i][self.j - 1]
        self.tiles[self.i][self.j - 1] = t

    def right(self):
        self.find_space()
        t = self.tiles[self.i][self.j]
        self.tiles[self.i][self.j] = self.tiles[self.i][self.j + 1]
        self.tiles[self.i][self.j + 1] = t

    def print_tile(self):
        for row in self.tiles:
            print(" ".join(map(str, row)))
        print()

def sorting(test_list_1, test_list_2):

    if(test_list_1[0] <= test_list_2[0]):
        return -1
    else:
        return 1
    
def main():
    tiles = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    initial_tile = Tile(tiles)
    initial_tile.find_space()
    initial_tile.gn = 0
    pq = []
    pq.append([initial_tile.fn, initial_tile,[]])

    while pq:
        pq.sort(key = functools.cmp_to_key(sorting))
        t = pq.pop(0)
        path = t[2]
        if t[1].misplaced_tiles() == 0:
            cost = t[1].gn
            print(f"The cost is {t[1].gn + 1}")
            print("The optimal path by A*: ", end = '')
            for i in range(0,len(path)):
                if i != len(path)-1:
                    print(f"{path[i]} -> ", end = '')
            print(path[-1])
            break
        row, column = t[1].find_space()
        if row - 1 >= 0:
            i = Tile(t[1].tiles)
            i.up()
            i.gn = len(path)
            i.calculate_fn()
            pq.append([i.fn, i, path+['Up']])
        if row + 1 < 3:
            i = Tile(t[1].tiles)
            i.down()
            i.gn = len(path)
            i.calculate_fn()
            pq.append([i.fn, i, path+['Down']])
        if column - 1 >= 0:
            i = Tile(t[1].tiles)
            i.left()
            i.gn = len(path)
            i.calculate_fn()
            pq.append([i.fn, i, path+['Left']])
        if column + 1 < 3:
            i = Tile(t[1].tiles)
            i.right()
            i.gn = len(path)
            i.calculate_fn()
            pq.append([i.fn, i, path+['Right']])

if __name__ == "__main__":
    main()
