import json
import urllib.parse
import urllib.request


def get_coordinates(city):
    """Find latitude and longitude for a city."""

    encoded_city = urllib.parse.quote(city)

    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={encoded_city}&count=1&language=en&format=json"
    )

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        if "results" not in data:
            return None

        location = data["results"][0]

        return {
            "name": location["name"],
            "country": location.get("country", "Unknown"),
            "latitude": location["latitude"],
            "longitude": location["longitude"]
        }

    except Exception:
        return None


def get_weather(latitude, longitude):
    """Get current weather information."""

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,weather_code,wind_speed_10m"
        "&timezone=auto"
    )

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())

    except Exception:
        return None


def weather_description(code):
    """Convert weather code into readable text."""

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    return weather_codes.get(code, "Unknown weather")


def display_weather(location, weather):
    """Display weather information."""

    current = weather["current"]

    temperature = current["temperature_2m"]
    feels_like = current["apparent_temperature"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]
    code = current["weather_code"]
    time = current["time"]

    description = weather_description(code)

    print("\n" + "=" * 50)
    print("              WEATHER INFORMATION")
    print("=" * 50)

    print(f"Location       : {location['name']}, {location['country']}")
    print(f"Time           : {time}")
    print(f"Condition      : {description}")
    print(f"Temperature    : {temperature} °C")
    print(f"Feels Like     : {feels_like} °C")
    print(f"Humidity       : {humidity}%")
    print(f"Wind Speed     : {wind_speed} km/h")

    print("=" * 50)


def main():
    print("=" * 50)
    print("             WEATHER INFORMATION APP")
    print("=" * 50)

    while True:
        city = input("\nEnter city name (or type 'exit'): ").strip()

        if city.lower() == "exit":
            print("\n👋 Thanks for using Weather App!")
            break

        if not city:
            print("❌ Please enter a city name.")
            continue

        print("\n🔎 Finding location...")

        location = get_coordinates(city)

        if location is None:
            print("❌ City not found or connection failed.")
            continue

        print("🌐 Getting current weather...")

        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        if weather is None:
            print("❌ Unable to get weather information.")
            continue

        display_weather(location, weather)


if __name__ == "__main__":
    main()
