import requests
import speech_recognition as sr
from config import API_KEY

def next_forecast(data):
        print("📅 Next 2-Day Forecast:")
        for day in data['forecast']['forecastday'][1:]:
            date = day['date']
            condition = day['day']['condition']['text']
            min_temp = day['day']['mintemp_c']
            max_temp = day['day']['maxtemp_c']
            print(f"📅 {date}: {condition} | Min: {min_temp}°C, Max: {max_temp}°C")

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&alerts=yes&aqi=yes"
    response = requests.get(url)
    data = response.json()

    with open("weather_conditions.json", "w", encoding="utf-8") as f:
        f.write(response.text)
    code = data['current']['condition']['code']
    def get_weather_emoji(code):
        if code == 1000:
            return "☀️"  # Sunny
        elif code == 1003:
            return "🌤️"  # Partly cloudy
        elif code in [1006, 1009]:
            return "☁️"  # Cloudy / Overcast
        elif code in [1030, 1135, 1147]:
            return "🌫️"  # Mist / Fog
        elif code in [1063, 1150, 1153, 1180, 1183, 1186, 1189, 1192, 1195, 1240, 1243, 1246]:
            return "🌧️"  # Rain / Showers
        elif code in [1066, 1069, 1114, 1117, 1210, 1213, 1216, 1219, 1222, 1225, 1255, 1258]:
            return "❄️"  # Snow
        elif code in [1087, 1273, 1276, 1279, 1282]:
            return "⛈️"  # Thunder
        elif code in [1171, 1201, 1207, 1237, 1261, 1264]:
            return "🌨️"  # Heavy snow / sleet / ice pellets
        elif code in [1198, 1168]:
            return "🧊"  # Freezing rain
        else:
            return "🌈"  # Default fallback
    emoji = get_weather_emoji(code)

        
    if "error" in data:
        print(f"❌ Couldn't find weather info for that city.\nError from API: {data['error']['message']}")
        return
    
    if 'air_quality' in data['current']:
        aqi = data['current']['air_quality']['gb-defra-index']
    else:
        print("⚠️ Air Quality Index data not available.")

    if 'forecast' in data:
        sunrise = data['forecast']['forecastday'][0]['astro']['sunrise']
        sunset = data['forecast']['forecastday'][0]['astro']['sunset']
        day_night = data['forecast']['forecastday'][0]['astro']['is_sun_up']
        if day_night == 1:
            D="🌞 It's daytime!"
        else:
            N="🌜 It's nighttime!"
    else:
        print("❌ Forecast data not available. Please check city or API key.")

    def rain_warning(data):
        try:
          will_rain = data['forecast']['forecastday'][0]['day'].get('daily_will_it_rain', 0)
          return "☔ Yes" if will_rain == 1 else "🌂 No"
        except:
          return "⚠️ Unknown"

    def will_snow(data):
        try:
         will_snow = data['forecast']['forecastday'][0]['day'].get('daily_will_it_snow', 0)
         return "❄️ Yes" if will_snow == 1 else "☃️ No"
        except:
         return "⚠️ Unknown"

        
    today = data['forecast']['forecastday'][0]['date']
    print("\n" + "═"*70)
    print(f"📅 Weather Forecast for {today} in {data['location']['name']}, {data['location']['region']}, {data['location']['country']}:")
    print("" + "═"*70)
    print(f"timezone: {data['location']['tz_id']} | Local Time: {data['location']['localtime']}")
    print("" + "═"*70)
    print(f"n🌍 Location: {data['location']['name']},{data['location']['region']}, {data['location']['country']}")
    print(f" Cloud Coverage: {data['current']['cloud']}%")
    print(f"Will Rain: {rain_warning(data)} | Will Snow: {will_snow(data)}")
    print(f"🌤 Weather:{get_weather_emoji(code)} {data['current']['condition']['text']} ")
    print(f"Air Quality Index(1-10): {data['current']['air_quality']['gb-defra-index']}")
    print(f"🌡 Temperature: {data['current']['temp_c']}°C ({data['current']['temp_f']}°F) | Min: {data['forecast']['forecastday'][0]['day']['mintemp_c']}°C , Max:{data['forecast']['forecastday'][0]['day']['maxtemp_c']}°C ")
    print(f"🌡 Feels Like: {data['current']['feelslike_c']}°C ({data['current']['feelslike_f']}°F)")
    print(f"☀️ UV Index: {data['current'].get('uv', 'N/A')}")
    print(f"💧 Humidity: {data['current']['humidity']}%")
    print(f"🌬 Wind Speed: {data['current']['wind_kph']} km/h")
    print(f"🌅 Sunrise: {sunrise} & 🌇 Sunset: {sunset}")
    print(f"📅 Last Updated: {data['current']['last_updated']}\n")
    print("" + "═"*50)
    next_forecast(data)
    print("🌈 Have a great day! 🌈\n")

# --- Chatbot loop ---
print("👋 Welcome to WeatherBot! (type 'exit' to quit) & (type 'mylog' to see Search History)")
history = []

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak the city name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        city = recognizer.recognize_google(audio)
        print(f"🗣 You said: {city}")
        return city
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand. Try again.")
        return None
    except sr.RequestError:
        print("❌ API unavailable.")
        return None
    
mode = input("Type 'voice' to use microphone or press Enter for 'text': ")

while True:
    if mode.lower() == "voice":
        city = get_voice_input()
        if city is None:
            continue
        # ✅ Check if voice input is exit
        if city.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Stay safe.")
            break
    else:
        city = input("🌐 Enter city name: ").strip().lower()
        if city in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Stay safe.")
            break
    if city is None:
        continue
    if city=='mylog':
        print(f"📝 Search History: ",history)
        break
        
    get_weather(city)
    history.append(city)

