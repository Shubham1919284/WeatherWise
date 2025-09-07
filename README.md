# 🌦️ Voice-Enabled Weather Model

A Python-based **AI-powered weather assistant** that delivers **real-time 3-day forecasts** using the **WeatherAPI**.  
The app supports both **voice input 🎤** (via SpeechRecognition) and **text input ⌨️**, providing a friendly, emoji-rich experience with detailed weather insights such as temperature, AQI, sunrise/sunset times, and rain/snow alerts.  

---

## ✨ Key Features
- 🎤 **Voice or text input** → Ask for a city name by speaking or typing  
- 🌐 **Real-time 3-day forecasts** powered by [WeatherAPI](https://www.weatherapi.com/)  
- 🌞 **Comprehensive details** → Sunrise/sunset, “feels like” temp, humidity, wind  
- 🌧️ **Rain & snow alerts** → Stay informed about upcoming conditions  
- 📊 **Air Quality Index (AQI)** classification → Good, Moderate, Poor, etc.  
- 🧠 **Session history tracking** → Keeps a short memory of searches  
- 😎 **Clean CLI interface** → Emoji-enhanced summaries for quick readability  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **SpeechRecognition** 🎙️  
- **pyttsx3** (Text-to-Speech, optional) 🔊  
- **requests** (API handling) 🌐  
- **WeatherAPI** ☁️  
- **JSON & Regex** (data parsing and filtering)  

---

## 📂 Project Structure
- `main.py` → Main chatbot script  
- `requirements.txt` → Required dependencies  
- `README.md` → Documentation (this file)  

---

## 🚀 Getting Started

Follow these steps to set up and run the project:  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shubham1919284/Voice-Weather-Chatbot.git
cd Voice-Weather-Chatbot
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your WeatherAPI key

Open `main.py` and replace the placeholder:

```python
API_KEY = "your_api_key_here"
```

### 4️⃣ Run the chatbot

```bash
python main.py
```

---

## 🌟 Example Output

📍 **Input:** *“Delhi”*

🌡️ **Temperature:** 32°C (feels like 35°C)
💧 **Humidity:** 72%
💨 **Wind:** 14 km/h
☀️ **Sunrise/Sunset:** 05:52 / 18:49
🌧️ **Alert:** Light rain expected tomorrow
📊 **AQI:** Moderate 😷

---

## 📸 Screenshots

![Screenshot 1](https://github.com/Shubham1919284/WeatherWise/blob/32d2bed1529945a7c0b199e38ccc68f26e4aa08d/Screenshot%202025-06-29%20133630.png)
![Screenshot 2](https://github.com/Shubham1919284/WeatherWise/blob/32d2bed1529945a7c0b199e38ccc68f26e4aa08d/Screenshot%202025-06-29%20133724.png)

---

## 📝 Notes

* 🎙️ If microphone access fails, the chatbot will **fall back to text input**
* 🌍 Requires stable internet connection (real-time data fetched from WeatherAPI)
* 🔑 Get a free API key at [WeatherAPI.com](https://www.weatherapi.com/)

---

## 👨‍💻 Author

**Shubham Kumar Jha**  
BTech CSE (Data Science) | Gulzar Group of Institutes (PTU)  

📧 Email: [sk1919284@gmail.com](mailto:sk1919284@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/shubham-kumar-jha-1a2b3c](https://www.linkedin.com/in/shubham-kumar-jha-1a2b3c)  
🔗 GitHub: [github.com/Shubham1919284](https://github.com/Shubham1919284)  


