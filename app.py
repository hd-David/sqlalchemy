from sqlalchemy import Table, Column,Integer, String, ForeignKey,Numeric, MetaData
from sqlalchemy import create_engine, insert, update, delete
from sqlalchemy.orm import sessionmaker,relation
from sqlalchemy.ext.declarative import declarative_base
Base  = declarative_base()


class Nation(Base):
    __tablename__ = "nation"
    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    

class County(Base):
    __tablename__ = "county"
    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    # define the relationship between Nation and County
    nation = relation("Nation", backref= "county")
    nation_id = Column(Integer, ForeignKey("nation.id"))

def dbconnect(): # establishing the connection to the database
    engine = create_engine("sqlite:///my.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session() 

