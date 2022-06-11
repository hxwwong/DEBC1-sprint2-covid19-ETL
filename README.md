# COV1D-19 Philippine Data Pipeline

# Description and Objective

These are the scripts used for a centralized data pipeline using Philippine COVID-19 data that is deployed in our GCP project for the second sprint for the ESK DEBC1. 

The scripts are run once day at XX:XX:XX AM UTC+8

**Data Sources**: This list is the complete list of sources that the data is pulled from.
- Aggregated data sources:
  - Fact Rackers News: https://www.factrakers.org/search-results?q=Covid
  - Covid 19- Fact Checks Rappler:https://www.rappler.com/topic/covid-19-fact-checks/
  - COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University: https://github.com/CSSEGISandData/COVID-19
  - Our World In Data: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Philippines.csv
- Non-aggregated data sources: 
  - Republic of Philippines Department of Health: https://doh.gov.ph/covid19tracker
  - Philippine Statistics Authority: https://psa.gov.ph/issip-stat-domain/demographic-and-social-statistics


# Dynamic Use of the APIs 
* Insert challenges encountered with APIs
* add a general guide on how we can troubleshoot the API if may issues
* how to modify code for the APIs

# How to Configure the Scheduled Pulls / information  

# Use cases for the data 

# Webscraping 
* Limitations: Each script is applicable to a specific website domain (e.g rappler.py: https://www.rappler.com/topic/covid-19-fact-checks/, factrackers.py:https://www.factrakers.org/search-results?q=Covid)
* How to run:
  - python rappler.py
  - python factrackers.py
