from flask import Flask, send_from_directory, jsonify
import requests
import os

app = Flask(__name__, static_folder='templates/static')

def get_api_key():
    secret_path = '/run/secrets/owm_api_key'
    if os.path.exists(secret_path):
        with open(secret_path, 'r') as f:
            return f.read().strip()
    return os.getenv('OWM_API_KEY')

API_KEY = get_api_key()
CANADIAN_CITIES = ['Toronto', 'Vancouver', 'Montreal']

@app.route('/weather')
def get_weather():
    weather_data = []
if not API_KEY:
    raise ValueError("API key missing! Set OWM_API_KEY env var or Docker Secret.")

CANADIAN_CITIES = [
    "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa",
    "Edmonton", "Winnipeg", "Quebec City", "Halifax", "Victoria"
]

@app.route('/')
def serve_react():
    return send_from_directory('templates', 'index.html')  # Serve React's build

@app.route('/weather')
def get_weather():
    weather_data = []
        for city in CANADIAN_CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},CA&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                "city": city,
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            })
        return jsonify(weather_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5022)