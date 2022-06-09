#!/bin/bash

wget -O vaccination_$(date +%d-%m-%Y).csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Philippines.csv
