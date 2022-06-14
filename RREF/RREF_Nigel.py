
from tkinter import N


class RREF_Matrix():
    matrix = []
    def createMatrix(self, row, column):
        #self.matrix = [[0 for x in range(row)] for y in range(column)] 
        self.matrix = [[8,2,3], [4,5,6], [7, 8, 9]]

    def printer(self):
        for n in self.matrix:
            for m in n:
                print(m, end = " ")
            print()
    def ValueLocation(self, i, j, value):
        if(value != ''):
            self.matrix [i][j] = value
        else:
            value = 0
            self.matrix [i][j] = value
    
    def getMatrix(self):
        return self.matrix


    def rref(self, rows, columns, diag, rowbase):
        if rows < len(self.matrix) and columns < len(self.matrix[rows]):
            if rows == diag and columns == diag:
                sub = self.matrix[rows][columns] - 1 
                print(f"R{rows + 1} - {sub}")
                for columns in range(len(self.matrix[rows])):
                    self.matrix[rows][columns] = self.matrix[rows][columns] - sub
                    diag = diag + 1
            else:
                sub = self.matrix[rows - rowbase][columns] * self.matrix[rows][columns]
                print(f"R{rows + 1} - {sub}")
                for columns in range(len(self.matrix[rows])):
                    self.matrix[rows][columns] = self.matrix[rows][columns] - sub
                rowbase = rowbase + 1
            
            if rows < len(self.matrix) and columns < len(self.matrix[rows]):
                rows = rows + 1
                columns = 0
            elif rows == len(self.matrix) - 1 and columns < len(self.matrix[rows]):
                columns = columns + 1
                rows = 0
            matrix.printer()
            matrix.rref(rows, columns, diag, rowbase)
        else: 
            return
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
matrix.rref(rows, columns, diag, rowbase)
