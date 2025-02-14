#!/bin/bash


psql -U sculptor_user -d sculptor -c "CREATE TABLE table1 (id SERIAL PRIMARY KEY, name VARCHAR(100));"

