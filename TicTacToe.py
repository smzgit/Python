class Player:
    def __init__(self,n,s):
        self.name = n
        self.symbol =  s
        self.moves = 0
        print("\n******* ",n," -- Player ready !! *******\n")

class Board:
    board = []
    def __init__(self):
        for i in range(3):
            li = ["[ ]"]*3
            self.board.append(li)

    def displayBoard(self):
        print("\t\t\t\t","0  1  2")
        for i in range(len(self.board)) :
            print("\t\t\t",i,"-",end="")
            for j in self.board[i] :
                print(j,end="")
            print()

    def canEnter(self,r,c,sym):
        if  r<0 or r> len(self.board)-1:
            return False
        if  c<0 or c> len(self.board)-1:
            return False
        if  self.board[r][c] != "[ ]":
            return False
        else:
            return True

    def checkVictory(self,p):
        smm = "["+p.symbol+"]"

        for j in range(3):
            for i in self.board[j]:
                if i == smm:
                    continue
                else:
                    break
            else:
                return True

        for j in range(3):
            for i in range(3):
                if self.board[i][j] == smm:
                    continue
                else:
                    break
            else:
                return True

        if  (self.board[0][0]==smm and self.board[1][1]==smm and self.board[2][2]==smm ):
            return True
        if  (self.board[0][2]==smm and self.board[1][1]==smm and self.board[2][0]==smm ):
            return True
        else:
            return False



    def play(self,p1,p2):

        while(True) :
            print("\n____________________________________________________________\n")
            print(p1.name," ! Enter Positions(Row & Column ) to place your symbol")
            row = int(input("Row : "))
            col = int(input("Column :"))
            p1.moves+=1
            flag = self.canEnter(row, col, p1.symbol)
            if(flag)  :
                self.board[row][col] = '['+p1.symbol+']'
            else:
                while(not flag) :
                    print("\tWrong Position Entered !! Enter again(Row & Column) ")
                    row = int(input("Row : "))
                    col = int(input("Column :"))
                    flag = self.canEnter(row, col, p1.symbol)
                    if (flag):
                        self.board[row][col] = '[' + p1.symbol + ']'

            self.displayBoard()
            if(self.checkVictory(p1)):
                    print("\n\tHurray !! ",p1.name,"  is Winner !!\n")
                    break

            if (p1.moves + p2.moves)>=8:
                print("Game Draw !!!")
                break

            print("____________________________________________________________\n")
            print(p2.name," ! Enter Positions(Row & Column ) to place the symbol")
            row = int(input("Row : "))
            col = int(input("Column :"))
            p2.moves += 1
            flag = self.canEnter(row, col, p2.symbol)
            if (flag):
                self.board[row][col] = '[' + p2.symbol + ']'
            else:
                while (not flag):
                    print("\tWrong Position Entered !! Enter again(Row & Column) ")
                    row = int(input("Row : "))
                    col = int(input("Column :"))
                    flag = self.canEnter(row, col, p2.symbol)
                    if (flag) :
                        self.board[row][col] = '[' + p2.symbol + ']'
            self.displayBoard()
            if (self.checkVictory(p2)):
                    print("\n\tHurray !! ",p2.name," is Winner !!\n")
                    break




def main():
    symbols = {"X","O"}
    print("\n*********** Welcome ***********")
    print("******* Tic Tac Toe Game *******")
    print("__________________________________\n")
    b = Board()
    print(" Board : ")
    b.displayBoard()

    print("First Player")
    p1name = input("Enter your name : ")
    p1symbol = input("Select a symbol(X or O) : ").upper()
    p1 = Player(p1name,p1symbol)

    print("Second Player\n2. Select a symbol(X or O)")
    p2name = input("Enter your name : ")
    p2symbol = symbols.difference(p1symbol).pop()
    print(p2name," your symbol is ", p2symbol)
    p2 = Player(p2name, p2symbol)

    b.play(p1,p2)

main()