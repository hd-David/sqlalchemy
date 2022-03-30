from app import Nation, County, dbconnect
from sqlalchemy import create_engine, insert, update, delete, select
import pprint

pp = pprint.PrettyPrinter(indent=4)

session = dbconnect()
# getting contents of objects from the database
nation = session.query(Nation).filter(Nation.name == "Tanzania").all()

pp.pprint(nation)