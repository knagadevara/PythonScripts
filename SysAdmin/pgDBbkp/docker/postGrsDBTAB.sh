#!/usr/bin/env bash

#read -p "Postgres user name: " name
#read -s -p "Postgres user password: " password
POSTGRES_USER="knagadevara"
POSTGRES_PASSWORD="Sai1991"
POSTGRES_DB="company_2020"
container_Name="postgres"

echo "Creating database container"
sudo docker volume rm pg-data
sudo docker volume create pg-data
sudo docker run -d \
  --name ${container_Name} \
  -e POSTGRES_USER=${POSTGRES_USER} \
  -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
  -e POSTGRES_DB=${POSTGRES_DB} \
  -e PGDATA="/var/lib/postgresql/data/pgdata" \
  -v "pg-data:/var/lib/postgresql/data" \
  -p "5432:5432" \
  --restart always \
  postgres:9.6-alpine

sleep 20 # Ensure enough time for postgres database to initialize and create role

c_DB="${PWD}/CreateDB.sql"
c_TAB="${PWD}/company_2020.sql"

if [[ ! -f $c_DB  || ! -f $c_TAB ]] ; then
echo "Required SQL dump file missing"
exit 1
fi

echo "creating a Database ${POSTGRES_DB}"
sudo docker exec -i ${container_Name} psql -U ${POSTGRES_USER} -d ${container_Name} < $c_DB
echo "creating a Table in Database ${POSTGRES_DB}"
sudo docker exec -i ${container_Name} psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < $c_TAB
echo "Checking the count of data in Table"
psql ${container_Name}://${POSTGRES_USER}:${POSTGRES_PASSWORD}@127.0.0.1:5432/${POSTGRES_DB} -c "SELECT count(id) FROM employees;"
