from models import House


def main():
    my_house = House(address={'address_data': {
        'house_number': 1023,
        'street_name': "Main Street",
        'city_name': "Anytown"
    }})

    my_house.validate()

main()
