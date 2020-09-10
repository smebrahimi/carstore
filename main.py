#from car import Car
import datetime

class Car:
    def __init__(self):
        self.list_car = ['BMW X5', 'Audi A4']

    def add(self):
        item = raw_input('''Insert new a car ''')
        if not item in self.list_car:
            self.list_car.append(item)
            print('added.')
        else:
            print('Car is already exist.')
        init()

    def show_all(self):
        print(self.list_car)
        init()


class Parking:
    number_all_available = 1

    def __init__(self):
        self.parking_lot = [
            {'id': 1, 'name': 'BMW i3', 'price': 2000, 'date': '2020-09-10 12:11:19.074303'},
            {'id': 2, 'name': 'Audi a7', 'price': 3000, 'date': '2020-08-10 12:11:19.074303'},
            {'id': 3, 'name': 'Hyundai i10', 'price': 1000, 'date': '2020-09-14 12:11:19.074303'},
            {'id': 4, 'name': 'Lexus rx 350', 'price': 4000, 'date': '2020-09-15 12:11:19.074303'}
        ]

    def add_car(self):
        if len(self.parking_lot) < self.__class__.number_all_available:
            car_name = raw_input('''Please insert a car name ''')
            car_price = raw_input('''Please insert price ''')
            car_date = datetime.datetime.now()
            dictionary = {
                "name": car_name,
                "price": car_price,
                "date": car_date
            }
            dict_copy = dictionary.copy()
            self.parking_lot.append(dict_copy)
            print(self.parking_lot)
            init()
        else:
            print('Parking is full')
            init()

    def show_all_cars(self):
        self.show_items(self.parking_lot)
        init()

    def sell_car(self):
        self.show_items()
        car_id = input('''
        - - - - - - - - - - - -
        Please select a car id for sell
        - - - - - - - - - - - - 
         ''')
        self.delete_car(car_id)
        self.show_all_cars()

    def show_chipset_car(self):
        cheapest_car = min(self.parking_lot, key=lambda x:x['price'])
        print('''
        - - - - - - - - - - - - - 
        Properties of Cheapest Car
        - - - - - - - - - - - - -
        ''')
        self.show_items([cheapest_car])
        init()

    def show_expensive_car(self):
        cheapest_car = max(self.parking_lot, key=lambda x:x['price'])
        print('''
        - - - - - - - - - - - - - 
        Properties of Expensive Car
        - - - - - - - - - - - - -
        ''')
        self.show_items([cheapest_car])
        init()

    def delete_selected_car(self):
        self.show_items()
        car_id = raw_input('''
        - - - - - - - - - - - -
        Please select a car id for delete
        - - - - - - - - - - - - 
        ''')
        self.delete_car(car_id)
        self.show_all_cars()

    def delete_car(self, car_id=0):
        self.parking_lot = [item for item in self.parking_lot if not (int(item['id']) == int(car_id))]

    @staticmethod
    def show_items(items=[]):
        for x in items:
            for k, v in x.items():
                print('{}: {}'.format(k, v))
            print('- - - - - -')


def switch(x):
    car = Car()
    parking = Parking()
    switch_case = {
        0: car.add,
        1: parking.add_car,
        2: parking.sell_car,
        3: parking.show_all_cars,
        4: parking.show_chipset_car,
        5: parking.show_expensive_car,
        6: parking.delete_selected_car,
        9: car.show_all
    }
    func = switch_case.get(x, 'no exist')
    return func()


def init():
    value = input('''
        What do you want to do?
        0- add a car store !
        1- add a car to parking
        2- sell a car
        3- show all cars in parking
        4- show the cheapest car
        5- show the most expensive car
        6- delete a car from parking
        7- how much money we made ?
        8- our history of sales
        9- all car stores
        10- merge car stores
        ''')
    switch(value)


init()
