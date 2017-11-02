"""
    mimesis needs to be installed: 'python -m pip install mimesis'

    This module generates dummy data and inserts it into database.
"""
from mimesis import Personal, Datetime, Address
from mimesis.builtins import USASpecProvider


def generate_fake_persons(size):
    """ This function generates a list of dummy persons
        (email, username, fullname, DOB, address and ssn)
    """
    person = Personal('en')
    datetime = Datetime()
    address = Address('en')
    usa_provider = USASpecProvider()

    fake_persons = []
    for _ in range(0, size):
        fake_person = {}
        fake_person['email'] = person.email()
        fake_person['uname'] = person.username()
        fake_person['fname'] = person.full_name()
        fake_person['dob'] = datetime.date(1970, 2000)
        fake_person['address'] = address.address() + " - " + address.state()
        fake_person['ssn'] = usa_provider.ssn()
        fake_persons.append(fake_person)

    return fake_persons


if __name__ == "__main__":
    for _ in generate_fake_persons(5):
        print(_)