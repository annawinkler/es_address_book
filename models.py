from elasticsearch_dsl import Document, InnerDoc, Integer, Keyword, Nested


class AddressParts(InnerDoc):
    house_number = Integer(required=True)
    street_name = Keyword(required=True)
    city_name = Keyword(required=True)

    def validate(self):
        print('House number {} street name {} city name {}'.format(self.house_number, self.street_name, self.city_name))
        if self.house_number < 0:
            raise RuntimeError('Not a valid house number!')
        else:
            return True


class AddressData(InnerDoc):
    address_data = Nested(AddressParts, required=True)

    def validate(self):
        print("Validating address data...")
        # AddressParts(**self.address_data.to_dict()).validate()
        for part in self.address_data:
            part.validate()
        return True


class House(Document):
    address = Nested(AddressData, required=True)

    def validate(self):
        print("Validating my house...")
        # AddressData(**self.address.to_dict()).validate()
        for a in self.address:
            a.validate()
        return True
