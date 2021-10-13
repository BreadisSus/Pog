 

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []


    def add_passenger(self, name):
        if not self.openseats():
            return False 
        self.passengers.append(name)
        return True 

    def openseats(self):
        return self.capacity - len(self.passengers)



sus = Flight(3)

nice = (["big chungus", "pewdiepie", "wow", "no"])
 
##why wont this work why ahy dsdfaioafss i am dead dying and dead dead edaed
for people in nice:
    if Flight.add_passenger(nice):
        print(f"added{people} to flight")
    else:
        print(f"their aint no seats, suck my nutz {people}")
