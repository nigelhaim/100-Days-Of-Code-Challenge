class RREF_Matrix():
    matrix = []
    def createMatrix(self, row, column):
        #self.matrix = [[0 for x in range(row)] for y in range(column)] 
        self.matrix = [[1,2,3], [4,5,6], [7, 8, 9]]

    def printer(self):
        for n in self.matrix:
            for m in n:
                print(m, end = "\t")
            print()
    def ValueLocation(self, i, j, value):
        if(value != ''):
            self.matrix [i][j] = value
        else:
            value = 0
            self.matrix [i][j] = value
    
    def getMatrix(self):
        return self.matrix


    def rref(self):
        if not self.matrix: return
        lead = 0
        row_Count = len(self.matrix)
        col_Count = len(self.matrix[0])
        for r in range(row_Count):
            if col_Count <= lead:
                return
            i = r
            while self.matrix[i][lead] == 0:
                i = i + 1
                if i == row_Count:
                    i = r
                    lead = lead + 1
                    if col_Count == lead:
                        return
            if i != r:
                self.matrix[i] = self.matrix[r]
                self.matrix[r] = self.matrix[i]
            divisor = self.matrix[r][lead]
            for self.matrixdivr in self.matrix[r]:
                self.matrix[r] = self.matrixdivr / divisor
            for j in range(row_Count):
                if j != r:
                    subtrahend = self.matrix[j][lead]
                    for k in range(col_Count):
                        self.matrix[j][k] = self.matrix[j][k] - (subtrahend * self.matrix[r][k])
            lead += 1
            matrix.printer()
            print()
rows = int(input("Number of rows: "))
columns = int(input("Number of Columns: "))
diag = 0
rows = 0
columns = 0
rowbase = 1
matrix = RREF_Matrix()
matrix.createMatrix(rows, columns)
matrix.printer()

#print("Please in put the values for the matrix: ")

#for n in range(rows):
#    for m in range(columns):
#        value = input(f"Value of location [{n}][{m}]: ")
#        matrix.ValueLocation(m, n, value)
#        matrix.printer()
print("Matrix RREF")
matrix.rref()
matrix.printer()