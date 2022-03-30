from app import Nation, County, dbconnect
from sqlalchemy.sql.expression import update
import pprint

pp = pprint.PrettyPrinter(indent=4)

session = dbconnect()

#Replacing Morroco with Tanzania
session.query(Nation).filter(Nation.name == "Morroco").\
    update({"name": "Tanzania"}, synchronize_session="fetch")
session.commit()
#checking the updated data
resu = session.query(Nation.name).all()
pp.pprint(resu)