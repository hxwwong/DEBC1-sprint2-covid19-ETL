import pandas as pd 
import numpy as np 

pop = pd.read_csv('population_by_municipality.csv')

pop['highly_urbanized'] = pop['province'].apply(lambda x: 1 if x =='high' else 0)
pop['province'] = pop['province'].apply(lambda prov: 'NA' if prov == 'high' else prov)

pop.to_csv('population_by_municipality_final.csv', index=False) 