class Vehicle:
    def start(self):
        print("Starting the vehicle")


class Car(Vehicle):
    def start(self):
       
        print("Starting the car engine.")
        print("Checking all systems.")
        print("Car is ready to go!")


def main():
    print("Vehicle behavior:")
    v = Vehicle()
    v.start()

    print("\nCar behavior:")
    c = Car()
    c.start()

if __name__ == "__main__":
    main()