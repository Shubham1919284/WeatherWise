🌦️ Voice-Enabled Weather Model

A Python-based weather model that provides real-time 3-day forecasts using WeatherAPI. It supports both voice input (via SpeechRecognition) and text input, returning detailed weather data including temperature, AQI, sunrise/sunset, rain/snow alerts, and more—all with intuitive emoji-based output.

🚀 Features
🎤 Voice or text input for city names

🌐 Fetches real-time weather data from WeatherAPI

🌞 Includes comprehensive data: sunrise/sunset times, "feels like" temperature, humidity, and wind speed

🌧️ Detects and alerts on rain/snow forecasts

📊 Provides AQI (Air Quality Index) classification (Good, Moderate, Poor, etc.)

🧠 Tracks search history within a session

😊 Features a clean command-line interface with emoji-enhanced summaries

🔧 Technologies Used
Python: Core programming language

SpeechRecognition: For handling voice input

pyttsx3: For text-to-speech functionality (optional)

requests: To interact with the WeatherAPI

WeatherAPI: The source for all weather data

JSON & Regex: For data handling and filtering

## 📥 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Shubham1919284/Voice-Weather-Chatbot.git
cd Voice-Weather-Chatbot
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Add your WeatherAPI key
```bash

Open main.py and replace the placeholder with your actual API key:
API_KEY = "your_api_key_here"
```

4. Run the chatbot
```bash
python main.py
```

📝 Important Notes
You may need to install system-level dependencies for PyAudio to work correctly.

Ensure your microphone is properly configured for voice input.

The pyttsx3 library is for text-to-speech. If you don't want this feature, you can remove it from your requirements.txt and the main.py file.

📃 requirements.txt
The dependencies for this project can be installed from the following list:
requests
SpeechRecognition
pyaudio
pyttsx3

----
### 👨‍💻 Author

**Shubham Kumar Jha**
BTech CSE (Data Science) | Gulzar Group of Institutes (PTU)

  - 📧 **Email:** `sk1919284@gmail.com`
  - 🔗 **LinkedIn:** `linkedin.com/in/shubham-kumar-jha-1a2b3c`
  - 🔗 **GitHub:** `github.com/Shubham1919284`


