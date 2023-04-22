# Weather App
The app is written in Python to get the current weather in location.

This application works in two different modes based on the user's input. If the user provides the city name e.g. `Prague` or in case of a city name composed of multiple words, use `'` e.g. `'Mladá Boleslav'` the application will display the weather for a given location.

The second mode does not require the user to enter a city name. The application then uses the city name from an IP address.

## Usage
You can use this application by running:
```
python weather-app.py [-h] [-c CITY] key
```
- __python__ is a local instance of the Python interpreter
- __weather-app.py__ is the name of the application
- __-h__ is used for displaying a help message
- __-c__ is used for providing the city name, argument is optional
- __key__ API key for [Weather API](https://openweathermap.org/api), registration is required, and argument is mandatory

## Output
OpenWeatherMap provides extensive weather information about location, but in this case, the application parses out only the most relevant information for personal use therefore only *Weather Description*, *Temperature*, *Humidity*, and *Wind Speed* are displayed.

## Examples
* All examples expect a fully functional and legitimate API key from OpenWeatherMap otherwise it will not work.
* API keys are omitted from examples for security reasons
```
python .\weather-app.py 1...Z

City: Prague (CZ) @ 11:43
Weather: Clear
Temperature: 17°C
Humidity: 48%
Wind 3.6 m/s
```
```
python .\weather-app.py 1...Z -c 'Mladá Boleslav'

City: Mladá Boleslav (CZ) @ 11:48
Weather: Clear
Temperature: 18°C
Humidity: 49%
Wind 4.18 m/s
```