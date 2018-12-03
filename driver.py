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

    my_house.validate()

main()
