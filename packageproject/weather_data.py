import sys
import urllib.parse
import requests
from requests.models import Response

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates. Return one city (or None)'''

    response = requests.get(BASE_URI +
                            f'/api/location/search/?query={query}').json()
    if response == []:
        return None
    return response[0]


def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    response = requests.get(BASE_URI + f'/api/location/{woeid}/').json()
    return response['consolidated_weather']


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    woeid = search_city(query)['woeid']
    city = search_city(query)
    weather = weather_forecast(woeid)

    print(f"Here's the weather in London")
    for i in range(5):
        print(
            f"{weather[i]['applicable_date']}: {weather[i]['weather_state_name']} {round(weather[i]['the_temp'], 1)}"
        )


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
