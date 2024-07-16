class Car :

    def __init__(self,name,price,capacity: int,color,model) -> None:
        self.name = name
        self.price = price
        self.capacity = capacity
        self.color = color
        self.model = model

    def __str__(self) -> str:
        return f"{self.name},{self.price},{self.capacity},{self.color},{self.model}"

    def setPrice(self,price) :
        self.price = price

    def setName(self,name) :
        self.name = name

    def getPrice(self) :
        print(self.price)

    def getName(self) :
        print(self.name)

    def setCapacity(self,capacity) :
        self.capacity = capacity

    def getCapacity(self) :
        print(self.capacity)

    def setColor(self,colr) :
        self.color = colr

    def getColor(self) :
        print(self.color)

    def setModel(self,model) :
        self.model = model

    def getModel(self) :
        print(self.model)

class Adress :

    def __init__(self,country,city,street) -> None:
        self.country = country
        self.city = city
        self.street = street

    def __str__(self) :
        return f"{self.country},{self.city},{self.street}"

    def getCountry(self) :
        print(self.country)

    def setCountry(self,country) :
        self.country = country

    def getCity(self) :
        print(self.city)

    def setCity(self,city) :
        self.city = city

    def getStreet(self) :
        print(self.street)

    def setStreet(self,street) :
        self.street = street

class CarShowroom :

    def __init__(self,adress,name) -> None:
        self.adress = adress
        self.car = []
        self.name = name
        self.rating = []
    
    def __str__(self) :
        return f"{self.name},{self.adress},{len(self.car)},{self.getAvarageRating()}"

    def addCar(self,carname: str) -> None:
        self.car.append(carname)

    def removeCar(self,carname: str) -> bool:
        if carname in self.car :
            self.car.remove(carname)
        else :
            return False

    def getCarsInfo(self) -> None:
        for i in self.car :
            print(i,end =',')

    def getAdress(self) -> None:
        print(self.adress)

    def changeName(self,newName: str) -> None:
        self.name = newName

    def getName(self) -> None:
        print(self.name)

    def rate(self,rate: int) -> bool:
        if 0 < rate <= 5 :
            self.rating.append(rate)
        else :
            return False
        
    def getAvarageRating(self) -> int:
        x = sum(self.rating) / len(self.rating)
        return x

# car = Car("BMW",30000,7,"Red","M3")
# car = Adress("German","Berlin","21 avenue")
# car = CarShowroom("Tashkent","Carway")
# print(car)
# car.setPrice(20000)
# car.setName("Mers")
# car.setCapacity(6)
# car.setColor("blue")
# car.setModel("Maybach")
# car.getPrice()
# car.getName()
# car.getCapacity()
# car.getColor()
# car.getModel()
# car.setCountry("Russia")
# car.setCity("Moskva")
# car.setStreet("Labzak 21")
# car.getCountry()
# car.getCity()
# car.getStreet()
# car.addCar("Bmw")
# car.changeName("Rent Car")
# car.getName()
# car.rate(4)
# car.getCarsInfo()
# car.getAdress()
# car.getAvarageRating()
# car.removeCar("Bmw")
# car.getCarsInfo()