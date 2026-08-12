import tkinter as tk
import requests
import os
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime


API_KEY = os.getenv("OPENWEATHER_API_KEY")

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


class WeatherApp:

    def __init__(self, root):

        self.window = root
        self.window.title("Weather App")
        self.window.geometry("850x700")
        self.window.resizable(False, False)

        self.unit = "metric"
        self.current_data = None
        self.weather_icon = None



        title = tk.Label(
            root,
            text="Weather App",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=15)



        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Enter city:",
            font=("Arial", 13)
        ).grid(row=0, column=0, padx=5)

        self.city_entry = tk.Entry(
            input_frame,
            width=25,
            font=("Arial", 13)
        )
        self.city_entry.grid(row=0, column=1, padx=5)

        self.get_button = tk.Button(
            input_frame,
            text="Get Weather",
            font=("Arial", 12, "bold"),
            command=self.get_weather
        )
        self.get_button.grid(row=0, column=2, padx=5)



        self.unit_button = tk.Button(
            root,
            text="Switch to Fahrenheit",
            command=self.toggle_unit
        )
        self.unit_button.pack(pady=5)



        self.status_label = tk.Label(
            root,
            text="Enter a city to get weather information.",
            font=("Arial", 11)
        )
        self.status_label.pack(pady=5)



        self.current_frame = tk.LabelFrame(
            root,
            text="Current Weather",
            font=("Arial", 14, "bold"),
            padx=15,
            pady=10
        )
        self.current_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.icon_label = tk.Label(self.current_frame)
        self.icon_label.pack(side="left", padx=20)

        self.weather_text = tk.Label(
            self.current_frame,
            text="",
            font=("Arial", 13),
            justify="left"
        )
        self.weather_text.pack(side="left", padx=20)



        self.hourly_frame = tk.LabelFrame(
            root,
            text="Next 6 Hours",
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10
        )
        self.hourly_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.hourly_text = tk.Text(
            self.hourly_frame,
            height=6,
            width=90,
            font=("Arial", 10)
        )
        self.hourly_text.pack()



        self.daily_frame = tk.LabelFrame(
            root,
            text="Next 5 Days",
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10
        )
        self.daily_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.daily_text = tk.Text(
            self.daily_frame,
            height=8,
            width=90,
            font=("Arial", 10)
        )
        self.daily_text.pack()


    def get_weather(self):

        city = self.city_entry.get().strip()

        # Empty input validation
        if city == "":
            self.show_error("Error: City name cannot be empty.")
            return

        # API key validation
        if not API_KEY:
            self.show_error(
                "Error: OPENWEATHER_API_KEY is not configured."
            )
            return

        self.status_label.config(
            text="Fetching weather...",
            fg="black"
        )

        try:


            current_params = {
                "q": city,
                "appid": API_KEY,
                "units": self.unit
            }

            response = requests.get(
                CURRENT_URL,
                params=current_params,
                timeout=5
            )

            data = response.json()

            if response.status_code == 404:
                self.show_error("Error: City not found.")
                return

            if response.status_code == 401:
                self.show_error("Error: Invalid API key.")
                return

            if response.status_code != 200:
                self.show_error(
                    "Error: " +
                    data.get("message", "Something went wrong.")
                )
                return

            self.current_data = data

            self.display_current_weather(data)

            forecast_params = {
                "q": city,
                "appid": API_KEY,
                "units": self.unit
            }

            forecast_response = requests.get(
                FORECAST_URL,
                params=forecast_params,
                timeout=5
            )

            forecast_data = forecast_response.json()

            if forecast_response.status_code != 200:
                self.show_error(
                    "Could not load forecast."
                )
                return

            self.display_hourly_forecast(
                forecast_data
            )

            self.display_daily_forecast(
                forecast_data
            )

            self.status_label.config(
                text="Weather updated successfully.",
                fg="green"
            )

        except requests.exceptions.Timeout:

            self.show_error(
                "Error: Request timed out."
            )

        except requests.exceptions.ConnectionError:

            self.show_error(
                "Error: No Internet connection."
            )

        except (requests.exceptions.RequestException, KeyError, TypeError, ValueError) as e:

            self.show_error(
                "Unexpected Error: " + str(e)
            )


    def display_current_weather(self, data):

        city = data["name"]

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        condition = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        icon_code = data["weather"][0]["icon"]

        try:

            icon_url = (
                f"https://openweathermap.org/img/wn/"
                f"{icon_code}@2x.png"
            )

            icon_response = requests.get(
                icon_url,
                timeout=5
            )

            image = Image.open(
                BytesIO(icon_response.content)
            )

            image = image.resize((100, 100))

            self.weather_icon = ImageTk.PhotoImage(image)

            self.icon_label.config(
                image=self.weather_icon
            )

        except (requests.exceptions.RequestException, OSError, ValueError):

            self.icon_label.config(
                image=""
            )

        unit_symbol = "°C"

        if self.unit == "imperial":
            unit_symbol = "°F"

        self.weather_text.config(
            text=
            f"City: {city}\n"
            f"Temperature: {temperature:.2f} {unit_symbol}\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {condition.title()}\n"
            f"Wind Speed: {wind_speed:.2f} "
            f"{'m/s' if self.unit == 'metric' else 'mph'}"
        )

    def display_hourly_forecast(self, data):

        self.hourly_text.delete(
            "1.0",
            tk.END
        )

        forecasts = data["list"][:2]

        for forecast in forecasts:

            date_time = datetime.fromtimestamp(
                forecast["dt"]
            )

            time_text = date_time.strftime(
                "%I:%M %p"
            )

            temperature = forecast["main"]["temp"]

            condition = forecast["weather"][0][
                "description"
            ]

            unit_symbol = "°C"

            if self.unit == "imperial":
                unit_symbol = "°F"

            self.hourly_text.insert(
                tk.END,
                f"{time_text} | "
                f"{temperature:.1f}{unit_symbol} | "
                f"{condition.title()}\n"
            )

    def display_daily_forecast(self, data):

        self.daily_text.delete(
            "1.0",
            tk.END
        )

        daily_data = {}

        for forecast in data["list"]:

            date = datetime.fromtimestamp(
                forecast["dt"]
            ).strftime("%Y-%m-%d")

            if date not in daily_data:
                daily_data[date] = forecast

        count = 0

        for date, forecast in daily_data.items():

            if count >= 5:
                break

            date_object = datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            day_name = date_object.strftime(
                "%A"
            )

            temperature = forecast["main"]["temp"]

            condition = forecast["weather"][0][
                "description"
            ]

            unit_symbol = "°C"

            if self.unit == "imperial":
                unit_symbol = "°F"

            self.daily_text.insert(
                tk.END,
                f"{day_name} ({date})\n"
                f"  Temperature: "
                f"{temperature:.1f}{unit_symbol}\n"
                f"  Weather: "
                f"{condition.title()}\n\n"
            )

            count += 1

    def toggle_unit(self):

        if self.unit == "metric":

            self.unit = "imperial"

            self.unit_button.config(
                text="Switch to Celsius"
            )

        else:

            self.unit = "metric"

            self.unit_button.config(
                text="Switch to Fahrenheit"
            )

        # Refresh weather if a city is already loaded
        if self.city_entry.get().strip() != "":
            self.get_weather()

    def show_error(self, message):

        self.status_label.config(
            text=message,
            fg="red"
        )

app_window = tk.Tk()

app = WeatherApp(app_window)

app_window.mainloop()