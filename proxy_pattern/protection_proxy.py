"""
Protection proxy is a proxy class that controls access to a particular resource.
"""


class Car:  # underlying system
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:  # proxy on top of underlying system
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)  # encapsulates underlying object as an attribute

    def drive(self):  # conform to the API of the underlying object
        if self.driver.age > 16:  # add access control to the underlying system
            self._car.drive()
        else:
            print("Driver too young")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    driver = Driver("John", 12)
    # car = Car(driver)
    car = CarProxy(driver)
    car.drive()
