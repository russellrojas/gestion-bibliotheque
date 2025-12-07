import psycopg2


#user personnel
HOST= "localhost"
USER= "postgres"
PASSWORD= "russell96"
DATABASE= "postgres"


"""
#user UTC 
#note: activer VPN
HOST= "tuxa.sme.utc"
USER= "nf18a022"
PASSWORD= "sJ8L3MCwbQ92"
DATABASE= "dbnf18a022"
"""
try:
    com=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST,DATABASE,USER,PASSWORD))
    print("connexion réussie")

except OSError as e:
    print (e)
