"""
    mimesis needs to be installed: 'python -m pip install mimesis'

    This module generates dummy data and inserts it into database.
"""
from mimesis import Personal, Datetime, Address
from mimesis.builtins import USASpecProvider
import sqlite3


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
        fake_person = (person.email(), person.username(), person.full_name(), datetime.date(1970, 2000), \
                       address.address() + " - " + address.state(), usa_provider.ssn())
        fake_persons.append(fake_person)

    return fake_persons


def db_stuff(list_of_fake_persons):
    """ This function creates a connection to the SQLite database (in the current directory)
        and executes some basic SQL statements (create table, insert, select and drop table)
    """
    con = sqlite3.connect('test_baza.db')
    cursor = con.cursor()

    sql_create = 'CREATE TABLE peoples (email text, uname text, fname text, dob text, address text, ssn text)'
    cursor.execute(sql_create)
    con.commit()

    sql_insert = 'INSERT INTO peoples VALUES (?,?,?,?,?,?)'
    cursor.execute(sql_insert, list_of_fake_persons[0])
    cursor.executemany(sql_insert, list_of_fake_persons[1:])
    con.commit()
    print('Total number of rows inserted:', con.total_changes)

    sql_select = 'SELECT * FROM peoples'
    rows_cursor = cursor.execute(sql_select)
    for row in rows_cursor:
        print(row)

    sql_drop = 'DROP TABLE peoples'
    cursor.execute(sql_drop)
    con.commit()
    print('Total number of rows deleted:', con.total_changes)
    con.close()


if __name__ == "__main__":
    list_of_fake_persons = generate_fake_persons(5)
    db_stuff(list_of_fake_persons)