class Cell(object):
    def __init__(self):
        self.content =' '

    def set_cell_color(self, color):
        self.content = color + self.content + '\x1b[0m'

    def __str__(self):
        return str(self.content)
