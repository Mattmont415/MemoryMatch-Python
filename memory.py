import random


class Memory:
    """Here we go! Let's try to make a fun and easy memory game!
    Woo looo hooooo!!!"""


    def printBoard(brd):
        print("   A B C D")
        for x in range(4):
            print(str(x) + "| ", end='')
            for y in range(4):
                print(str(brd[x][y]) + " ", end = "")
            print()

    def getBoard():
        return brd

    def setBoard():
        brd = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
        return brd

    def randomizeItems():
        # Items   0,      1,      2,      3,      4,      5,      6,      7
        arr = ['@','@','#','#','$','$','%','%','&','&','?','?','=','=','+','+']
        #Why is this one not working but the next version does?
        # glass = [['X'] * 4] * 4
        glass = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]

        for i in range(len(arr)):
            x = random.randint(0,3)
            y = random.randint(0,3)
            if glass[x][y] == 'X':
                glass[x][y] = arr[i]
            else:
                while glass[x][y] != 'X':
                    x = random.randint(0,3)
                    y = random.randint(0,3)
                    if glass[x][y] == 'X':
                        glass[x][y] = arr[i]
                        break
        return glass

    def playGame(gbrd, rbrd):
        valinp1 = False
        valinp2 = False
        inp1 = ""
        inp2 = ""

        while Memory.checkWin(gbrd) == 0:
            while not valinp1:
                getinp1 = input("Make a valid first guess (number)(letter): ")
                getinp1 = getinp1.lower()
                inp1 = list(getinp1)
                if (len(inp1) == 2 and inp1[0] >= '0' and inp1[0] <= '3' and 
                        inp1[1] >= 'a' and inp1[1] <= 'd'):
                    #converts letters to numbers for use in brd list
                    inp1[1] = str(ord(inp1[1])-97)
                    x1 = int(inp1[0])
                    y1 = int(inp1[1])
                    if gbrd[x1][y1] == 'X':
                        gbrd[x1][y1] = rbrd[x1][y1]
                        Memory.printBoard(gbrd)
                        valinp1 = True
            while not valinp2:
                getinp2 = input("Make a valid second guess (number)(letter): ")
                getinp2 = getinp2.lower()
                inp2 = list(getinp2)
                if (len(inp2) == 2 and inp2[0] >= '0' and inp2[0] <= '3' and 
                        inp2[1] >= 'a' and inp2[1] <= 'd'):
                    #converts letters to numbers for accessing axis of list
                    inp2[1] = str(ord(inp2[1])-97)
                    x2 = int(inp2[0])
                    y2 = int(inp2[1])
                    if gbrd[x2][y2] == 'X':
                        gbrd[x2][y2] = rbrd[x2][y2]
                        Memory.printBoard(gbrd)
                        valinp2 = True
            
            #Check if a match, then remove the pieces from the gb
            if gbrd[x1][y1] == gbrd[x2][y2]:
                print("You got a match!")
                gbrd[x1][y1] = " "
                gbrd[x2][y2] = " "
                Memory.printBoard(gbrd)
                valinp1 = False
                valinp2 = False
                inp1 = ""
                inp2 = ""
                if Memory.checkWin(gbrd) == 1:
                    print("You win!")
                    return 1
            else:
                print("Sorry, no match!")
                gbrd[x1][y1] = "X"
                gbrd[x2][y2] = "X"
                Memory.printBoard(gbrd)
                valinp1 = False
                valinp2 = False
                inp1 = ""
                inp2 = ""

    def checkWin(gbrd):
        countwin = 0
        for x in range(4):
            for y in range(4):
                if gbrd[x][y] == " ":
                    countwin += 1
        if countwin == 16:
            return 1
        else:
            return 0



def main():
    print("Let's play memory! There are 8 symbols you need to match: \n" +
            "@, #, $, %, &, ?, =, +. Guess the symbols two at a time with \n" +
            "the pattern (row)(col), i.e. 0A, 2D, or 3C")
    playagain = True
    inpreplay = ""

    while playagain:
        gamebrd = Memory.setBoard()
        Memory.printBoard(gamebrd)
        randbrd = Memory.randomizeItems()
        Memory.playGame(gamebrd,randbrd)
        inpreplay = input("Want to play again? Y for yes, any other key for no")
        if inpreplay.lower() != 'y':
            playagain = False

if __name__ == "__main__":
    main()