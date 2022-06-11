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

* The data from the Philippine Statistics Authority was manually edited into tidy data format using Google Sheets and Microsoft Excel. This approach was necessary due to the variance in formatting and the presence of merged cells. 

* A short script, `add_urbanicity.py` was added to create a new data field `highly_urbanized` that identifies whether or not a particular city is classified as highly urbanized according to the Philippine Statistics Authority. This metric of urbanization is a relevant feature due to its relative prominence in predicting COVID-19 vulnerability and preparedness. 

# Dynamic Use of the APIs 
* Insert challenges encountered with APIs
* add a general guide on how we can troubleshoot the API if may issues
* how to modify code for the APIs

# How to Configure the Scheduled Pulls / information  

# Use cases for the data 
The data can be utilized for a variety of analytics involving local, municipal, regional, or national analytics. This includes demonstrating the use of fake news, and socio-demographic information as potential features for predicting certain outcomes related to COVID-19.


# Referenced Studies 
Mehta, M., Julaiti, J., Griffin, P., & Kumara, S. (2020). Early stage machine learning–based prediction of us county vulnerability to the covid-19 pandemic: Machine learning approach. JMIR Public Health and Surveillance, 6(3), e19446. https://doi.org/10.2196/19446

Pan, Y., Zhang, L., Yan, Z., Lwin, M. O., & Skibniewski, M. J. (2021a). Discovering optimal strategies for mitigating COVID-19 spread using machine learning: Experience from Asia. Sustainable Cities and Society, 75, 103254. https://doi.org/10.1016/j.scs.2021.103254

Pan, Y., Zhang, L., Yan, Z., Lwin, M. O., & Skibniewski, M. J. (2021b). Discovering optimal strategies for mitigating COVID-19 spread using machine learning: Experience from Asia. Sustainable Cities and Society, 75, 103254. https://doi.org/10.1016/j.scs.2021.103254

Tiwari, A., Dadhania, A. V., Ragunathrao, V. A. B., & Oliveira, E. R. A. (2021). Using machine learning to develop a novel COVID-19 Vulnerability Index (C19vi). Science of The Total Environment, 773, 145650. https://doi.org/10.1016/j.scitotenv.2021.145650

# Webscraping 
* Limitations: Each script is applicable to a specific website domain (e.g rappler.py: https://www.rappler.com/topic/covid-19-fact-checks/, factrackers.py:https://www.factrakers.org/search-results?q=Covid)
* How to run:
  - python rappler.py
  - python factrackers.py
