class Board:
    def __init__(self, data):
        self.data = data

    def board(self):
        lines = []

        for i in range(10):
            line = ''
            for j in range(10):
                line += str(self.data[i][j])
            lines.append(line)

        return '\n'.join(lines)


class Board:
    def __init__(self, data):
        self.data = data

    def board(self):
        buf = []
        self.collect_rows(buf)
        return ''.join(buf)

    def collect_rows(self, buf):
        for i in range(10):
            self.collect_row(buf, i)

    def collect_row(self, buf, row):
        for i in range(10):
            buf.append(str(self.data[row][i]))
        buf.append('\n')