#https://documenter.getpostman.com/view/11586746/SztEa7bL

import requests
api_url = "http://ergast.com/api/f1/drivers?=123"
response = requests.get(api_url)

response.raise_for_status()

data = response.json()

print(data)

f1driverdb: List[str,str,str, List[str]] = [
    (
        "Max Verstappen"
        "Netherlands"
        [
           "Red Bull"
           "EA Sports"
           "Heiken" 
        ],
    ),
]
