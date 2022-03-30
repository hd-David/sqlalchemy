from app import Nation , County, dbconnect
from sqlalchemy.sql.expression import delete
import pprint

pp = pprint.PrettyPrinter(indent=4)
#establishing a connection
session = dbconnect()
# deleting by using a name 
stmt = delete(Nation).where(Nation.name == "Sudan").execution_options(synchronize_session="fetch") 
session.execute(stmt)
session.commit()
