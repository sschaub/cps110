# Dependencies:
#   pip install requests

# Hartford Fire Incidents: https://data.hartford.gov/Public-Safety/FH_SOCRATA/anj2-ytvy


import requests
import csv

response = requests.get('https://data.hartford.gov/resource/824e-9vse.csv')

lines = response.text.split('\n')
reader = csv.reader(lines[1:])

for line in reader:
  alm_time = line[2]
  arv_time = line[4]
  print(alm_time, arv_time)

