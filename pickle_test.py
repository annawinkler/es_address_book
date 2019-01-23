import pickle

from models import House, AddressData, AddressParts


def main():
    my_house = House(
        address=[
            AddressData(
                address_data=[
                    AddressParts(
                        house_number=1023,
                        street_name="Main Street",
                        city_name="Anytown"
                    )
                ]
            )
        ]
    )

    # also called automatically when `.save()` is called
    my_house.full_clean()

    out = pickle.loads(pickle.dumps(my_house))
    out.full_clean()

    # clean also automatically wraps dicts in appropriate classes so this is
    # also acceptable:
    my_house = House(address=[{'address_data': [{
                'house_number': 1023,
                'street_name': "Main Street",
                'city_name': "Anytown"
            }]}])
    my_house.full_clean()

main()
