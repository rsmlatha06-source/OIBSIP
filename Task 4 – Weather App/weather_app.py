import requests

import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city name: ").strip()

if city == "":
    print("Error: City name cannot be empty.")

else:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)

        data = response.json()

        if response.status_code == 200:

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32

            humidity = data["main"]["humidity"]

            weather = data["weather"][0]["description"]

            wind_speed = data["wind"]["speed"]

            print("\n========== Weather Report ==========")
            print(f"City: {city.title()}")
            print(f"Temperature: {temperature_c:.2f} °C")
            print(f"Temperature: {temperature_f:.2f} °F")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather.title()}")
            print(f"Wind Speed: {wind_speed} m/s")

        elif response.status_code == 404:
            print("Error: City not found.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        else:
            print("Error:", data.get("message", "Something went wrong."))

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: No Internet connection.")

    except Exception as e:
        print("Unexpected Error:", e)