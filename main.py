from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone):
        if (not phone.isdigit()) or len(phone) != 10:
            raise ValueError
        self.value = phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                self.phones.remove(p)

    def edit_phone(self, phone_1, phone_2):
        for i in self.phones:
            if i.value == phone_1:
                i.value = phone_2
                return
        raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, value):
        self.data.update({value.name.value: value})

    def find(self, value):
        if value in self.data:
            return self.data[value]

    def delete(self, value):
        if value in self.data:
            del self.data[value]
