document.getElementById('searchBtn').addEventListener('click', function() {
    const city = document.getElementById('cityInput').value.trim();
    if (city === "") {
        document.getElementById('errorMessage').innerText = "Please enter a city name.";
        return;
    }

    fetchWeather(city);
});

function fetchWeather(city) {
    const weatherData = {
        "Bengaluru": {
            "temperature": 28,
            "description": "Cloudy",
            "humidity": 78,
            "windSpeed": 15,
            "pressure": 1015,
            "icon": "☁️"
        },
        "Kolkata": {
            "temperature": 15,
            "description": "Rainy",
            "humidity": 83,
            "windSpeed": 20,
            "pressure": 1012,
            "icon": "🌧️"
        },
        "Chennai": {
            "temperature": 32,
            "description": "Clear Sky",
            "humidity": 98,
            "windSpeed": 12,
            "pressure": 1002,
            "icon": "☀️"
        },
        "Mumbai": {
            "temperature": 25,
            "description": "Cloudy",
            "humidity": 80,
            "windSpeed": 16,
            "pressure": 1017,
            "icon": "☁️"
        },
        "Delhi": {
            "temperature": 19,
            "description": "Foggy",
            "humidity": 78,
            "windSpeed": 10,
            "pressure": 998,
            "icon": "🌧️"
        },
    };

    const data = weatherData[city];
    if (!data) {
        document.getElementById('errorMessage').innerText = "City not found.";
        document.getElementById('weatherData').innerHTML = "";
        return;
    }

    document.getElementById('errorMessage').innerText = "";
    document.getElementById('weatherData').innerHTML = `
        <h3>${city}</h3>
        <p>${new Date().toLocaleDateString()}</p>
        <p><strong>Temperature:</strong> ${data.temperature}°C</p>
        <p><strong>Description:</strong> ${data.description}</p>
        <p><strong>Humidity:</strong> ${data.humidity}%</p>
        <p><strong>Wind Speed:</strong> ${data.windSpeed} km/h</p>
        <p><strong>Pressure:</strong> ${data.pressure} hPa</p>
        <p>${data.icon}</p>
    `;
}

document.getElementById('backToTop').addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

