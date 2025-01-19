import requests

API_KEY = "YOUR_API_KEY"
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code != 200:
        print(f"Ошибка получения данных о погоде: {response.status_code}")
        return None

    return response.json()


def main():
    city = input("Введите название города: ")
    weather_data = get_weather(city)
    if weather_data:
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Текущая температура в {city}: {temp:.2f}°C")
        print(f"Описание погоды: {description}")


if __name__ == "__main__":
    main()
