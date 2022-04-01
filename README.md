Sqlachemy
In app.py, which is our model we are creating class instances to define objects which creates tables in the database.
We have two objects in our model, one is defining nations and the other one is county.
Then we define our connection to the database using session.
Using sessionmaker, we only define our connection once and we use the coonection anywhere we want to use it.

In create.py file - we are importing our model which is app.py.
Then we use session since it is our connection to have access to the database we defined in in the model.
We populate our database with data, this is where we are entering data into the database.
Then we add our data to the database by commiting.

In read.py - we import our model
Using session to gain access to the database
We run our view query depending on the data the user want to check

In delete.py - we import the model
Using session = dbconnect, we get access to our database
We can query the row we want to remove, in our case we are using the name whuich removes every row that equals the name.
Then we commit our delete for change to be effective.

Update.py - we import the model.
we use session to have access our data in the database.
We query the row we want to update, in this case we are changing the name of the natio.
We then do commit our transaction.


SQL documentation for CRUD
The SQL command below, creates a table in the database.
```
CREATE TABLE nation (
    id int,
    name varchar(255),
    capital_city varchar(255),
    population int,
);
```
Below ia the querry the user used to view data in the database.
One thing to keep in mind SQL is not case sensitive, you can use lowercase or uppercase it still works.
SELECT * FROM nation;
The command above is the view querry where we check all data in our database.

To delete data or row from our database we use the following querry.
DELETE FROM nation WHERE nation.name='Malawi';

To change data in one row we use update which is the SQL command.
UPDATE nation
SET nation.name='Tanzania'
WHERE nation.name='Morroco';
