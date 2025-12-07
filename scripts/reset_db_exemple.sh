# !/bin/bash

# run db_create.sql
PGPASSWORD=mdp psql -U nf18a023 -h tuxa.sme.utc -d dbnf18a023 -f db_create.sql

# run db_insert.sql
PGPASSWORD=mdp psql -U nf18a023 -h tuxa.sme.utc -d dbnf18a023 -f db_insert.sql

# run db_select.sql
PGPASSWORD=mdp psql -U nf18a023 -h tuxa.sme.utc -d dbnf18a023 -f db_select.sql
