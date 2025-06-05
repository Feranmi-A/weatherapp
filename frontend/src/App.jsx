import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [weather, setWeather] = useState([])

  useEffect(() => {
    fetch('/weather')
      .then(res => res.json())
      .then(data => setWeather(data))
  }, [])

  return (
    <div className="app">
      <h1>Canada Weather</h1>
      <div className="cities">
        {weather.map((city) => (
          <div key={city.city} className="city-card">
            <h2>{city.city}</h2>
            <img
              src={`http://openweathermap.org/img/wn/${city.icon}.png`}
              alt={city.description}
            />
            <p>{city.temp}°C, {city.description}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App