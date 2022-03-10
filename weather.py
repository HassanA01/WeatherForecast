import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "0f47f1e933659483531bf709cfdbe746"

KEL_TO_CEL = -273.15


def fetch_weather():

    city = input("Enter a city name: ")

    while city.upper() != "EXIT":
        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
        response = requests.get(request_url)

        if response.status_code != 200:
            print("An error ocurred.")
            return fetch_weather()
        else:
            data = response.json()
            weather = data["weather"][0]["description"]
            feels_like = round(data["main"]["feels_like"] + KEL_TO_CEL, 2)
            temp_cel = round(data["main"]["temp"] + KEL_TO_CEL, 2)
            wind = round(data["wind"]["speed"], 2)
            print(f'The current weather in {city} is currently {weather} with a temperature of {temp_cel} degrees '
                  f'Celsius and feels like {feels_like} with the wind going upto {wind} mph')

        city = input("Enter another city to check or 'exit' to quit the application: ")

    print("\nThank you for using the Weather App. Have a good day.")
    quit()


if __name__ == "__main__":
    fetch_weather()
