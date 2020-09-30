import datetime
import itertools


class Car:
    id_generator = itertools.count(1, 1)

    def __init__(self, name, model, price):
        self.id = next(Car.id_generator)
        self.name = name
        self.model = model
        self.price = price


class CarStore:
    id_generator = itertools.count(1, 1)
    sell_id_generator = itertools.count(1, 1)

    def __init__(self, name):
        self.id = next(CarStore.id_generator)
        self.name = name
        self.date = datetime.datetime.now()
        self.cars = []
        self.sales_history = []

    def add_car(self, name, model, price):
        car = Car(name, model, price)
        self.cars.append(car)
        print('Successfully add car to car store')

    def sell_car(self, car_id):
        item = [i for i in self.cars if (int(i.id) == int(car_id))][0]
        dictionary = {
            'id': next(CarStore.id_generator),
            'car': item,
            'date': datetime.datetime.now()
        }
        dict_copy = dictionary.copy()
        self.sales_history.append(dict_copy)
        self.delete_car(car_id)
        print('successfully sell car')

    def delete_car(self, car_id):
        self.cars = [i for i in self.cars if not (int(i.id) == int(car_id))]
        print('delete car from car store')

    def cheapest_car(self):
        return min(self.cars, key=lambda x: x.price)

    def expensive_car(self):
        return max(self.cars, key=lambda x: x.price)

    def all_cars(self):
        return self.cars


class App:
    def __init__(self):
        self.car_stores = []
        self.car_store = None

    def add_car_store(self):
        item = raw_input('Insert new a car store ')
        self.car_store = CarStore(item)
        self.car_stores.append(self.car_store)
        init()

    def add_car_to_store(self):
        name = raw_input('Insert new a car name ')
        model = raw_input('Insert new a car model ')
        price = raw_input('Insert new a car price ')
        self.car_store.add_car(name, model, price)
        init()

    def sell_car(self):
        self.print_all_cars()
        car_id = input('''
        - - - - - - - - - - - -
        Please select a car id for sell
        - - - - - - - - - - - - 
         ''')
        self.car_store.sell_car(car_id)
        init()

    def print_all_cars(self):
        for x in self.car_store.cars:
            print('- - - - - -')
            print('id: {} name: {} price: {}'.format(x.id, x.name, x.price))
            print('- - - - - -')

    def show_all_cars(self):
        self.print_all_cars()
        init()

    def show_chipset_car(self):
        item = self.car_store.cheapest_car()
        print('{} is cheapest car'.format(item.name))
        init()

    def show_expensive_car(self):
        item = self.car_store.expensive_car()
        print('{} is expensive car'.format(item.name))
        init()

    def delete_car_from_car_store(self):
        self.print_all_cars()
        car_id = input('''
        - - - - - - - - - - - -
        Please select a car id for delete
        - - - - - - - - - - - - 
         ''')
        self.car_store.delete_car(car_id)
        init()

    def get_money_made(self):
        # chera inja sum 0 has
        result = sum(int(obj['car'].price) for obj in self.car_store.sales_history)
        print('Money made {}'.format(result))
        init()

    def our_history_sales(self):
        print('- - - - - -')
        for obj in self.car_store.sales_history:
            print('In this date {}, you sold your {} car for ${}'.format(obj['date'], obj['car'].name, obj['car'].price))
            print('- - - - - -')
        init()

    def print_all_car_store(self):
        for x in self.car_stores:
            for k, v in x.items():
                print('{}: {}'.format(k, x))
            print('- - - - - -')

    def show_all_car_store(self):
        self.print_all_car_store()
        init()


app = App()


def switch(x):

    switch_case = {
        0: app.add_car_store,
        1: app.add_car_to_store,
        2: app.sell_car,
        3: app.show_all_cars,
        4: app.show_chipset_car,
        5: app.show_expensive_car,
        6: app.delete_car_from_car_store,
        7: app.get_money_made,
        8: app.our_history_sales,
        9: app.show_all_car_store
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
        ''')
    switch(value)


init()
