# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883
# openweather.py


import urllib, json
from urllib import request,error
from WebAPI import *


class LastFM(WebAPI):
    def __init__(self, artist="The_Weeknd"):
        self.artist = artist#this will be input

    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service

        '''
        self.apikey = apikey
        pass

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''
        if not self.apikey:
            raise ValueError("API key is not set. Please set the API key using the set_apikey method.")

        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={self.artist}&api_key={self.apikey}&format=json"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        self.first_track = data['toptracks']['track'][0]['name']

        return self.first_track

        # return trans
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


# # Invalid data formatting from the remote API
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        trans = self.load_data()
        messageTrans = message.replace("@lastfm", trans)
        return messageTrans

# TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API


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
    artist = "The_Weeknd"
    apikey = "92787b4240ee2a4885fa37de8647ca7b"
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={apikey}&format=json"

    last_fm = LastFM(artist)
    last_fm.set_apikey(apikey)
    last_fm.load_data()
    lastfm_object = _download_url(url)
    first_track = lastfm_object['toptracks']['track'][0]['name']
    print(first_track)


if __name__ == '__main__':
    main()
