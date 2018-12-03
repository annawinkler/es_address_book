from elasticsearch_dsl import Document, InnerDoc, Integer, Keyword, Nested, ValidationException


class AddressParts(InnerDoc):
    house_number = Integer(required=True)
    street_name = Keyword(required=True)
    city_name = Keyword(required=True)

    def clean(self):
        print('House number {} street name {} city name {}'.format(self.house_number, self.street_name, self.city_name))
        if self.house_number < 0:
            raise ValidationException('Not a valid house number!')


class AddressData(InnerDoc):
    address_data = Nested(AddressParts, required=True)


class House(Document):
    address = Nested(AddressData, required=True)
