import copy

class Board:
    def __init__(self, board=[[1,2,3],[4,5,6],[7,8,9]]):
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
            t.board[x][y]=i
            l.append(t)
        return l

    def check_x(self):
        d={}
        for row in self.board:
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
            if len(set(l))!=len(l):
                return False
        return True


    def check(self):
        return self.check_y() and self.check_x()











if __name__ == '__main__':
    b=Board()
    print(b.check())