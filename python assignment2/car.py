#Car rental system
class Car:
    def __init__(self,model,color,charge_per_hour):
        self.model=model
        self.color=color
        self.charge_per_hour=charge_per_hour
    def rental_charge(self,hours):
        return str(self.charge_per_hour*hours)
car1=Car("Bugatti Chiron","black",1000)
print('$' + car1.rental_charge(5))
