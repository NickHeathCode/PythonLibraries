class Table:
    _max_column_width = []
    headers = []
    data = []
    def __init__(self, *headers):
        self.headers = headers
        for header in headers:
            self._max_column_width.append(len(header) + 2)

    def addRow(self, *data):
        max_size = len(data) if len(data) < len(self.headers) else len(self.headers)
        self.data.append(data[0:max_size + 1])
        
        index = 0
        for datum in self.data[len(self.data) - 1]:
            if index >= len(self._max_column_width):
                break
            self._max_column_width[index] = self._max_column_width[index] if self._max_column_width[index] >= len(datum) + 2 else len(datum) + 2
            index += 1

    def printHeaders(self):
        for header in self.headers:
            print(header)

    def printData(self):
        for datum in self.data:
            print(datum)

    def print(self):
        separator = "├"
        for width in self._max_column_width:
            separator += "─"*width
            separator += "┼"

        separator = separator[0:-1]
        separator += "┤"

        # Top line
        print(separator.replace("├", "┌").replace("┼", "┬").replace("┤", "┐"))

        for i in range(len(self.headers)):
            header = self.headers[i]
            width = self._max_column_width[i]
            print("│ ", end="")
            print(header + " "*(width - 1 - len(header)), end="")

        print("│")

        # Header and data separator line
        print(separator.replace("├", "╞").replace("┼", "╪").replace("┤", "╡").replace("─", "═"))
        
        for j in range(len(self.data)):
            for i in range(len(self.headers)):
                try:
                    d = self.data[j][i]
                except:
                    d = ""
                    
                if i >= len(self._max_column_width):
                    break
                width = self._max_column_width[i]

                print("│ ", end="")
                print(d + " "*(width - 1 - len(d)), end="")

            print("│")
            if j < len(self.data) - 1:
                # Separator lines
                print(separator)

        # Bottom line
        print(separator.replace("├", "└").replace("┼", "┴").replace("┤", "┘"))