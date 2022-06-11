# COV1D-19 Philippine Data Pipeline

These are the scripts used for a centralized data pipeline using Philippine COVID-19 data that is deployed in our GCP project for the second sprint for the ESK DEBC1. 

The scripts are run once day at XX:XX:XX AM UTC+8

**Data Sources**: This list is the complete list of sources that the data is pulled from.
- Aggregated data sources:
  - Fact Rackers News: https://www.factrakers.org/search-results?q=Covid
  - COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University: https://github.com/CSSEGISandData/COVID-19
  - Our World In Data: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Philippines.csv
- Non-aggregated data sources: 
  - Republic of Philippines Department of Health: https://doh.gov.ph/covid19tracker
  - Philippine Statistics Authority: https://psa.gov.ph/issip-stat-domain/demographic-and-social-statistics
