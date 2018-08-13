# Dependencies:
#   pip install requests

# Hartford Fire Incidents: https://data.hartford.gov/Public-Safety/FH_SOCRATA/anj2-ytvy


import requests

response = requests.get('https://data.hartford.gov/resource/824e-9vse.json?alm_date=2015-10-13T00:00:00.000')

records = response.json()

for rec in records:
    print(rec['street'], rec['station'])

    