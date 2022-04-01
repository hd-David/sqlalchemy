from app import Nation, County, dbconnect

session = dbconnect()
# populating the table with some data
Malawi = Nation(
    name = "Malawi",
    capital_city = "lilongwe",
    population = 87432529

    )
Angola = Nation(
    name="Angola",
    capital_city = "Luanda",
    population = 98497895
    )

Ghana =  Nation(
    name="Ghana",
    capital_city = "Accra",
    population = 894366835
    )

Egypt =  Nation(
    name="Egypt",
    capital_city = "Cairo",
    population = 56673457
    )

Mali =  Nation(
    name="Mali",
    capital_city = "Bamako",
    population = 83989297
    )

Zimbabwe =  Nation(
    name = "Zimbabwe",
    capital_city = "Harare",
    population = 76538963
    )

Namibia  =  Nation(
    name = "Namibia",
    capital_city = "Windhoek",
    population = 78687535
    )

Congo =   Nation(
    name = "Congo",
    capital_city = "Kinshasa",
    population = 78439084
    )

Senegal =  Nation(
    name="Senegal",
    capital_city = "Dakar",
    population = 78696843
    )
    
session.add_all([Congo, Senegal, Namibia, Zimbabwe, Mali, Egypt,Ghana, Angola, Malawi]) # adding data to the session
session.commit()