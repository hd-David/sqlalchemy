from app import Nation, County, Town
from sqlalchemy.orm.exc import NoResultFound

def addGetNation(session, nation_name_input):
    # Try and get the Nation from the database. If error (Except) add to the database.
    try:
        nation = session.query(Nation).filter(Nation.name == nation_name_input).one()
    except NoResultFound:
        nation = Nation()
        nation.name = nation_name_input
    return nation

def addGetCounty(session, county_name_input, nation_name_input):
    # Try and get the County from the database. If error (Except) add to the database.
    try:
        county = session.query(County).filter(County.name == county_name_input).one()
    except NoResultFound:
        county = County()
        county.nation = addGetNation(session, nation_name_input)
        county.name = county_name_input
    return county