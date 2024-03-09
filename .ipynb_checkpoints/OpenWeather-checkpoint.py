# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883

import urllib, json
from urllib import request,error


class OpenWeather:
    def __init__(self, zipcode, ccode):
        self.zipcode = zipcode#this will be input
        self.country_code = ccode#this will be input
        self.apikey = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.sunset = None
        self.city = None

        
    
    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service

        '''
        #TODO: assign apikey value to a class data attribute that can be accessed by class members
        self.apikey = apikey
        pass

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''
        #TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
        if not self.apikey:
            raise ValueError("API key is not set. Please set the API key using the set_apikey method.")
        
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.country_code}&appid={self.apikey}&units=metric"
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        
        self.temperature = data['main']['temp']
        self.high_temperature = data['main']['temp_max']
        self.low_temperature = data['main']['temp_min']
        self.longitude = data['coord']['lon']
        self.latitude = data['coord']['lat']
        self.description = data['weather'][0]['description']
        self.humidity = data['main']['humidity']
        self.sunset = data['sys']['sunset']
        self.city = data['name']
        
        trans = self.description

        return trans
        #TODO: assign the necessary response data to the required class data attributes
        #use excpetions for"
        # Loss of local connection to the Internet
            #LossConnectionError
        # 404 or 503 HTTP response codes (indicating that the remote API is unavailable)

        # except HTTPError:
        #     print("404 Error. URL could not be found. Please try again.")
        #     url = input()
        # except ConnectionError:
        #     print("503 Error. Server is overloaded. Please try again.")
        #     url = input()


# Invalid data formatting from the remote API
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        trans = self.load_data()
        messageTrans = message.replace("@weather", trans)
        return messageTrans
        
#TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API


def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj


def main() -> None:
    zipcode = "92697"
    ccode = "US"
    apikey = "6af88070b5ade9132807d7d1f4b861a5"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"
    
    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    # print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
    # print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
    # print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
    # print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    # print(f"The current weather for {zipcode} is {open_weather.description}")
    # print(f"The current humidity for {zipcode} is {open_weather.humidity}")
    # print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")


    # weather_obj = _download_url(url)
    # if weather_obj is not None:
    #     description = weather_obj['weather'][0]['description']# need the [0] bc its a list
    #     # temperature = weather_obj['main']['temp']
    #     # pressure = weather_obj['main']['pressure']
    #     # humidity = weather_obj['main']['humidity']
    #     print(description)


# {'coord': {'lon': -117.8387, 'lat': 33.6485}, 
#  'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 
#  'base': 'stations', 
#  'main': {'temp': 288.37, 'feels_like': 287.98, 'temp_min': 286.94, 'temp_max': 289.8, 'pressure': 1013, 'humidity': 78}, 
#  'visibility': 10000, 
#  'wind': {'speed': 3.6, 'deg': 230}, 
#  'clouds': {'all': 75}, 'dt': 1709861264, 
# 'sys': {'type': 1, 'id': 5876, 'country': 'US', 'sunrise': 1709820699, 'sunset': 1709862784}, 
#  'timezone': -28800, 
#  'id': 0, 
#  'name': 'Irvine', 
#  'cod': 200}


if __name__ == '__main__':
    main()

