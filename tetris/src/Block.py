class Block:

    def __init__(self, label, matrix, color):
        self.label = label
        self.matrix = matrix # matrice 4x4 de boolean: si c'est une ligne -> 
        # true, false, false ,false
        # true, false, false, false
        # true, false, false, false
        # true, false, false, false
        self.color = None
        self.topLeftPos = 10

    def getBoxesPos(self):
        boxes = []

        rowIndex = 0
        for row in self.matrix:
            rowIndex += 1

            columnIndex = 0
            for item in row:
                
        
        return boxes

    def moveLeft(self):
        pass

    def moveRight(self):
        pass
    
    def moveDown(self):
        pass
