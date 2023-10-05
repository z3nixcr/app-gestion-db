from pony.orm import *

db = Database()
filename = 'data/system.db'


class Product(db.Entity):
    id = PrimaryKey(int)
    name = Required(str)
    description = Required(str)
    specification = Required(str)


db.bind(provider='sqlite', filename=filename, create_db=True)
db.generate_mapping(create_tables=True)
