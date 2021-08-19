import copy
import math

#hej
class Board:
    def __init__(self, board=[[1,2,3,5],[5,6,7,8],[9,10,11,12],[13,14,15,0]]):
        self.board = board
    def __str__(self):
        row_str=''
        for row in self.board:
            temp_row=''
            for col in row:
                temp_row+=str(col)
            temp_row+='\n'
            row_str+=temp_row

        return (row_str.rstrip())

    def create_children(self):
        x=0
        y=0

        while self.board[x][y] != 0 and x < len(self.board):
            y += 1
            if y == len(self.board):
                x += 1
                y = 0

        l=[]

        for i in range(len(self.board)):
            t=copy.deepcopy(self)
            t.board[x][y]=i+1
            l.append(t)
        return l

    def check_x(self):

        for row in self.board:
            row = [i for i in row if i != 0]
            if len(row) != len(set(row)):
                return False
        return True

    def check_y(self):
        ls=[]

        for j in range(len(self.board)):
            l = []
            for i in range(len(self.board[j])):
                l.append(self.board[i][j])
            ls.append(l)


        for l in ls:
            l=[i for i in l if i != 0]
            if len(set(l))!=len(l):
                return False
        return True


    def check(self):
        return self.check_y() and self.check_x()

    def is_filled(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return False
        else:
            return True
    def is_complete(self):
        return self.check() and self.is_filled() and self.check_squares()

    def check_squares(self):
        length=int(math.sqrt(len(self.board)))
        for j in range(length):
            for k in range(length):
                if (self.check_square(j*length,k*length,length))== False:
                    return False
        return True
    def check_square(self, j,k,length):
        l=[]
        for o in range(length):
            for p in range(length):
                l.append(self.board[j+o][p+k])
        l=l=[i for i in l if i != 0]
        return len(set(l))==len(l)















if __name__ == '__main__':
    b=Board()

    for i in b.create_children():
        print(i)
        print()
