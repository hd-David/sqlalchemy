from app import Nation, County, dbconnect

session = dbconnect()
# populating the table with some data
objects = [
    Nation(name="Malawi"),
    Nation(name="Angola"),
    Nation(name="Ghana"),
    Nation(name="Egypt"),
    Nation(name="Mali"),
    Nation(name="Zimbabwe"),
    Nation(name="Namibia"),
    Nation(name="Congo"),
    Nation(name="Senegal"),
    ]
session.bulk_save_objects(objects) # adding data to the session
session.commit()