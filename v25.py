class Shape :

    def __init__(self,symbol: str ,length: int) -> None:
        self.symbol = symbol
        self.length = length

    def setSymbol(self,symbol: str) -> None:
        self.symbol = symbol

    def setLength(self,length: int) -> None:
        self.length = length

class Line(Shape) :

    def __init__(self, symbol, length) -> None:
        super().__init__(symbol, length)

    def show(self) :
        for i in range(self.length) :
            print(self.symbol,end = " ")

class Triangle(Shape) :

    def __init__(self, symbol, length) -> None:
        super().__init__(symbol, length)

    def show(self) :
        for i in range (1, self.length+1) :
            print(i * (self.symbol + " "))

class Rectangle(Shape) :

    def __init__(self, symbol, length) -> None:
        super().__init__(symbol, length)

    def show(self) :
        for j in range(self.length) :
            for i in range(self.length) :
                print(self.symbol,end = " ")
            print("")

class NullShape(Shape) :

    def __init__(self, symbol, length) -> None:
        super().__init__(symbol, length)

    def show(self) :
        print("Bo'sh shakl")


sym = NullShape('*',5)

sym.show()