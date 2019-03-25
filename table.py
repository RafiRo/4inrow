from cell import Cell


class Table(object):
    place_in_table = None
    def __init__(self, x=7, y=6):
        self.table = [[Cell() for _ in range(x)] for _ in range(y)]
        self.x = x
        self.y = y
        self.place_in_table = x*y
    def __str__(self):

        separetor = '#'
        ptable='\n'
        for i in range(self.x):
            ptable = ptable + '  ' + str(i+1) + ' '
            separetor = separetor + '####'
        ptable = ptable + "\n"
        for i in range(self.y):
            ptable = ptable + separetor + "\n#"
            for j in range(self.x):
                ptable = ptable + " " + str(self.table[i][j]) + " #"
            ptable = ptable + "\n"
        ptable = ptable + separetor + "\n"
        return ptable

    def check_table(self, color, x, y):
        counter = 1
        temp_x = x
        temp_y = y

        ### Calc Row
        for _ in range(4):
            temp_x = temp_x + 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        temp_x = x
        for _ in range(4):
            temp_x = temp_x - 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        if counter > 3:
            return True
        temp_x = x

        ### Calc Col
        counter = 1
        for _ in range(4):
            temp_y = temp_y + 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        temp_y = y
        for _ in range(4):
            temp_y = temp_y - 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        if counter > 3:
            return True
        temp_y = y


        ### Calc diagonal 1
        counter = 1
        for _ in range(4):
            temp_x = temp_x + 1
            temp_y = temp_y + 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        temp_x = x
        temp_y = y
        for _ in range(4):
            temp_x = temp_x - 1
            temp_y = temp_y - 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        if counter > 3:
            return True
        temp_x = x
        temp_y = y

        ### Calc diagonal 2
        counter = 1
        for _ in range(4):
            temp_x = temp_x + 1
            temp_y = temp_y - 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        temp_x = x
        temp_y = y
        for _ in range(4):
            temp_x = temp_x - 1
            temp_y = temp_y + 1
            try:
                if color not in self.table[temp_y][temp_x].content:
                    break
                counter = counter + 1
            except IndexError:
                break
        if counter > 3:
            return True

        print(counter)
        return None

    def put_in_row(self, color, x):
        j = 0
        x = int(x) - 1

        if self.table[0][x].content != ' ':
            return "Row Is Full"

        for j in reversed(range(self.y)):

            if self.table[j][x].content != ' ':
                continue
            else:
                break
        self.place_in_table = self.place_in_table - 1
        self.table[j][x].set_cell_color(color)
        return self.check_table(color, x, j)

