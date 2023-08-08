import requests

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def plu_number_correlation(weather_data):
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    weather_description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    # Correlation logic based on weather conditions
    if temperature >= 30 and humidity >= 70:
        return "PLU: 1234 - Tropical and humid weather"
    elif temperature >= 25 and weather_description == "Clear":
        return "PLU: 5678 - Warm and sunny weather"
    elif temperature < 10 and wind_speed > 15:
        return "PLU: 9101 - Cold and windy weather"
    else:
        return "PLU: N/A - No specific correlation"

def retail_recommendations(weather_data):
    weather_description = weather_data["weather"][0]["description"]

    if "rain" in weather_description:
        return "Umbrellas and raincoats are recommended."
    elif "snow" in weather_description:
        return "Warm clothing and snow boots are recommended."
    elif "clouds" in weather_description:
        return "Consider offering indoor promotions or sales."
    elif "clear" in weather_description:
        return "Promote outdoor products and activities."

    return "No specific retail recommendations."

def main():
    api_key = "YOUR_API_KEY"

    city_name = input("Enter the city name: ")

    try:
        weather_data = get_weather_data(api_key, city_name)
        plu_number = plu_number_correlation(weather_data)
        retail_recommendation = retail_recommendations(weather_data)

        print(f"Weather data for {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Description: {weather_data['weather'][0]['description']}")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print("Correlated PLU Number:", plu_number)
        print("Retail Recommendation:", retail_recommendation)
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError as e:
        print("Invalid response format from API:", e)

if __name__ == "__main__":
    main()
