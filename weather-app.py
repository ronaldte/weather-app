#!/usr/bin/env python
"""Script to fetch actuall weather for given city.

This is intended to be used as standalone script. Provides no interface for use within
other application.
"""

import argparse
import socket
import json
import datetime
import sys

__author__ = "Ronald Telmanik"

def check_response(r):
    """Simple check for valid response."""
    res = r.decode().split("\r\n")
    status_code = res[0].split(' ')[1]

    if status_code != '200':
        print("ERROR: response is incomplete")
        sys.exit(-1)
    
    return json.loads(res[-1])
    
def get_weather(data):
    """Prints particular information from JSON response."""
    if data is None:
        return "No weather information available at this time."

    if "name" in data:
        print(f"City: {data['name']}", end=' ')
        if "sys" in data and "country" in data["sys"]:
            print(f"({data['sys']['country']})", end=' ')
        if "timezone" in data:
            time = datetime.datetime.utcnow() + datetime.timedelta(seconds=data['timezone'])
            print(f"@ {time.strftime('%H:%M')}")
    
    if "weather" in data:
        w = data['weather']
        if len(w) > 0 and ("main") in w[0]:
            print(f"Weather: {w[0]['main']}")

    if "main" in data:
        if "temp" in data["main"]:
            print(f"Temperature: {int(data['main']['temp'])}°C")
        if "humidity" in data["main"]:
            print(f"Humidity: {data['main']['humidity']}%")

    if "wind" in data and 'speed' in data['wind']:
        print(f"Wind {data['wind']['speed']} m/s")


def fetch(host, port, req):
    """Simple HTTP communication, which sends GET request to given host:port."""
    msg = f"GET {req} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host, port))
            sock.sendall(msg.encode())
            res = sock.recv(4096)
        except socket.error as e:
            print(f"ERROR: socket communication failed {e}")
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data about weather")
    parser.add_argument("-c", "--city", dest="city", help="City for which to look weather for")
    parser.add_argument("key", help="OpenWeatherMap Api key")
    args = parser.parse_args()

    if args.city is None:
        res = fetch(host='ipinfo.io', port=80, req="/json")
        res_json = check_response(res)
        if res_json is not None and "city" in res_json:
            args.city = res_json["city"]     

    req = f"/data/2.5/weather?q={args.city}&appid={args.key}&units=metric"
    host = "api.openweathermap.org"
    port = 80  

    res_json = check_response(fetch(host, port, req))
    get_weather(res_json)