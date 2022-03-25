import psycopg2

#probeer de connectie te maken met de sql database
try:
    conn = psycopg2.connect("dbname=test user=postgres host=localhost password=GigaByte+14!")
except:
    print( "I am unable to connect to the database")

#maak de cursor aan
cur = conn.cursor()

# Variabele aanmaken voor alle commandes voor het droppen van de tables
product = ('''SELECT * FROM product''')

cur.execute(product)




def randomProduct():
    x = False
    while x == False:
        randomproduct = ("""SELECT * FROM product
                                ORDER BY RANDOM()
                                LIMIT 1""")
        cur.execute(randomproduct)
        randomP = cur.fetchone()
        if randomP[7] != None:
            x = True
    return randomP[7]


print(randomProduct())


# record = cur.fetchmany(10)
# x = 0
# for row in record:
#     x += 1
#     print(f"printing {x} row \n")
#     print("_id = ", row[0],)
#     print("brand = ", row[1],)
#     print('category = ', row[7],)
#     print('sub_category = ', row[8],)
#     print("price = ", row[5], "\n")

# Commit de commando's
conn.commit()








