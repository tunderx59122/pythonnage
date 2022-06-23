class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def getX(self) -> int:
        return self.x
    
    def getY(self) -> int:
        return self.y
    
    def moveX(self, xToAdd:int) -> None:
        x += xToAdd

    def moveY(self, yToAdd:int) -> None:
        y += yToAdd