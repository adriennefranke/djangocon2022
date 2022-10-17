from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
import random
import logging
import sys
from cars.models import Car
from car_parts.models import CarPart, CarPartCar
from sales.models import Sale

class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        seed_database(self)
        logging.info("Done seeding database")

def delete_data():
    '''
    Deletes all data from database
    '''
    logging.info("Deleting Car data...")
    Car.objects.all().delete()

    logging.info("Deleting Sale data...")
    Sale.objects.all().delete()

    logging.info("Deleting CarPart data...")
    CarPart.objects.all().delete()
    CarPartCar.objects.all().delete()

def create_car_data():
    '''
    Creates car data
    '''
    logging.info("Creating Car data...")
    mini_models = ['Mini Countryman', 'Mini Cooper S Clubman', 'Mini 5 Door', 'Mini 3 Door', 'Mini Paceman', 'Mini Cooper S', 'Mini JCW', 'Mini Coupe']
    years = [int(i) for i in range(1969, datetime.now().year)]
    prices = [float(i) for i in range(10000, 60000)]

    car = Car(model_name=random.choice(mini_models), year_released=random.choice(years), msrp=random.choice(prices))
    car.save()

def get_random_date(start_date, end_date):
    '''
    Returns a random date in between the start_date and end_date
    '''
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())),)

def create_sale_data():
    '''
    Creates sale data
    '''
    logging.info("Creating Sale data...")
    cars = Car.objects.all()
    sale_prices = [float(i) for i in range(10000, 60000)]

    sale = Sale(car=random.choice(cars), sale_price=random.choice(sale_prices), sale_date=get_random_date(start_date=datetime.strptime('1969-01-01', '%Y-%m-%d'), end_date=datetime.now()))
    sale.save()

def create_carpart_data():
    '''
    Creates car part data
    '''
    logging.info("Creating CarPart data...")
    carpart_names = ["Widget {}".format(i) for i in range(1, 50000)]
    carpart_prices = [float(i) for i in range(0, 2500)]

    carpart = CarPart(part_name=random.choice(carpart_names), part_price=random.choice(carpart_prices))
    carpart.save()

def create_carpartcar_data():
    '''
    Creates car part car data
    '''
    logging.info("Creating CarPartCar data...")
    carparts = CarPart.objects.all()
    cars = Car.objects.all()

    carpartcar = CarPartCar(car=random.choice(cars), car_part=random.choice(carparts))

    carpartcar.save()

def seed_database(self):
    '''
    Clear database and then seed it
    '''
    # Delete data
    delete_data()

    # Create car data
    for i in range(250):
        create_car_data()

    # Create sale data
    for i in range(10000):
        create_sale_data()

    # Create car part data
    for i in range(3000):
        create_carpart_data()

    # Create car part car data
    for i in range(5000):
        create_carpartcar_data()
