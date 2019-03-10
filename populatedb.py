import mysql.connector

cnx = mysql.connector.connect(user='admin', password='adminpassword',host='democrud.cohktb5ed2cp.us-east-1.rds.amazonaws.com', database='MyCRUDDemo')

cursor = cnx.cursor()

TABLES = {}

TABLES['articles'] = (
"""CREATE TABLE IF NOT EXISTS articles(
    id INT(8) AUTO_INCREMENT,
    title VARCHAR(20) NOT NULL,
    body VARCHAR(255),
    author VARCHAR(20),
    PRIMARY KEY (id)
)   ENGINE=INNODB;""")

TABLES['users'] = (
"""CREATE TABLE IF NOT EXISTS users(
    id INT(8) NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    name VARCHAR(24),
    email VARCHAR(24),
    pwd VARCHAR(24),
    PRIMARY KEY (id)
)   ENGINE=INNODB;""")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
