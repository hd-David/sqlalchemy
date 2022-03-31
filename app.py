from sqlalchemy import Table, Column,Integer, String, ForeignKey,Numeric, MetaData, Float
from sqlalchemy import create_engine, insert, update, delete
from sqlalchemy.orm import sessionmaker,relation
from sqlalchemy.ext.declarative import declarative_base
Base  = declarative_base()


class Nation(Base):
    __tablename__ = "nation"
    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    capital_city = Column(String(64))
    population = Column(Integer())
    

class County(Base):
    __tablename__ = "county"
    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    # define the relationship between Nation and County
    nation = relation("Nation", backref= "county")
    nation_id = Column(Integer, ForeignKey("nation.id"))


# County is a child of Country
class Town(Base):
    __tablename__ = 'town'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    grid_reference = Column(String(64))
    easting = Column(Integer)
    northing = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Integer)
    postcode_sector = Column(String(64))
    local_government_area = Column(String(64))
    nuts_region = Column(String(64))
    town_type = Column(String(64))
    # We define the relationship between town and County here.
    county = relation("County", backref="town")
    county_id = Column(Integer, ForeignKey('county.id'))



def dbconnect(): # establishing the connection to the database
    engine = create_engine("sqlite:///my.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session() 

