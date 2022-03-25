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
### droped table, maakt het makelijker om te testen ###
cur.execute("""DROP TABLE productcategory""")





def randomProductCategory():
    x = False
    ### select van product een random row ###
    while x == False:
        randomproduct = ("""SELECT * FROM product
                                ORDER BY RANDOM()
                                LIMIT 1""")
        cur.execute(randomproduct)
        randomP = cur.fetchone()
        ### pakt van de random row een colum van category, als het null is dan probeerd die een andere row ###
        if randomP[7] != None:
            x = True
    return randomP[7]


def tableMakerCategory():
    # Variabele aanmaken voor alle tables en hun inhoud
    table = (
        """create table productCategory(
                product_id varchar, 
                brand varchar,
                gender varchar,
                herhaalaankopen bool,
                _name varchar,
                selling_price integer,
                stock integer,
                category varchar,
                sub_category varchar,
                sub_sub_category varchar,
                weekdeal bool,
                product_size varchar,
                promos varchar,
                product_type varchar,
                primary key(product_id)
            );
        """)
    cur.execute(table)
    # Commit de commando's
    conn.commit()

def inserter():
    ### insert van product de producten met dezelfde category in productcategory ###
    category = randomProductCategory()
    print(category)
    datainserter = ("INSERT INTO productcategory SELECT * FROM product WHERE category = (%s) ")
    cur.execute(datainserter, (category,))
    return

def runAll():
    ### runt alle functies ###
    print(randomProductCategory())
    print(tableMakerCategory())
    print(inserter())
print(runAll())
print("\nAFGEROND\n")
# Commit de commando's
conn.commit()








