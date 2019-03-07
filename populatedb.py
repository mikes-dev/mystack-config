import mysql.connector

cnx = mysql.connector.connect(user='admin', password='adminpassword',host='democrud.cohktb5ed2cp.us-east-1.rds.amazonaws.com', database='MyCRUDDemo')

cursor = cnx.cursor()

Tables = {}

TABLES['articles'] = (
    "CREATE TABLE 'articles' ("
    "  'id' int(8) NOT NULL AUTO_INCREMENT,"
    "  'title' varchar(20) NOT NULL,"
    "  'body' varchar(500),"
    "  'author' varchar(24),"
    "  PRIMARY KEY ('article_id')"
    ") ENGINE=InnoDB")

TABLES['users'] = (
    "CREATE TABLE 'users' ("
    "  'id' int(8) NOT NULL AUTO_INCREMENT,"
    "  'username' varchar(20) NOT NULL,"
    "  'name' varchar(24),"
    "  'email' varchar(24),"
    "  'password' varchar(24),"
    "  PRIMARY KEY ('article_id')"
    ") ENGINE=InnoDB")
