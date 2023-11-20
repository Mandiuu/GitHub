import os
from dotenv import load_dotenv
load_dotenv()


import requests

API_KEY = ""

#What is the URL to the documentation?
url = "https//www.weatherapi.com/docs"
print(f"The URL is", url)

API_KEY = os.getenv("API_KEY")
#response = requests.get("https//www.weatherapi.com/docs")
#weather = response.json()

print(API_KEY)


#Make a request for the current weather where you are born, or somewhere you've lived.

url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Rancagua&aqi=no'
response = requests.get(url)
data = response.json()

#Print out the country this location is in.
#Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
#What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
#What URL would I use to request a 3-day forecast at Heathrow?
#Print the date of each of the 3 days you're getting a forecast for.
#Print the maximum temperature of each of the days.
#Print only the day with the highest maximum temperature.


