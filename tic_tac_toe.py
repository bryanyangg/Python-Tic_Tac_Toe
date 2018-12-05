class TTT:

    grid = None
    done = None

    def __init__(self):
        self.grid = self.newGrid()

    def newGrid(self):
        grid=[["-","-","-"],["-","-","-"],["-","-","-"]]
        return grid

    def printGrid(self,grid):
        for i in grid:
            ret ="|"
            for j in i:
                ret+=j
                ret+='|'
            print(ret)

    def updateGrid(self,grid,input_0):
        err = "Already have entry"
        
        row_num = int(input_0[1])
        col_num = int(input_0[3])
        while grid[row_num][col_num] != "-":
            print(str((row_num,col_num))+ " " + err)
            x = input("Please make a move --> (r,c, 'O or X'):")
            input_0 = x
            row_num = int(input_0[1])
            col_num = int(input_0[3])
        choice = input_0[5]
        grid[row_num][col_num] = choice
        self.printGrid(grid)
        return grid

    def isFinished(self,grid):
        ls = []
        for i in range(0,len(grid)):
            if "-" not in grid[i]:
                ls.insert(i, True)
            else: ls.insert(i, False)
        print(str(ls) + str(self.done))
        if False not in ls:
            self.done = True
            return True
        else: return False

game = TTT()
game.printGrid(game.grid)
game.done = False

x = input("Please make a move --> (r,c, 'O or X'):")
while x != '' and game.done==False:
    if game.isFinished(game.grid):
        game.done = True
        print("Game is Done LOL")
        break
    game.updateGrid(game.grid,x)
    x = input("Please make a move --> (r,c, 'O or X'):")
