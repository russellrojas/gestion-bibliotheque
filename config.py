import psycopg2


#user personnel
HOST= "your_localhost"
USER= "your_user"
PASSWORD= "your_password"
DATABASE= "your_data_base"

try:
    com=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST,DATABASE,USER,PASSWORD))
    print("connexion réussie")

except OSError as e:
    print (e)
