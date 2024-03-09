# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883

from abc import ABC, abstractmethod
import urllib, json
from urllib import request,error


class WebAPI(ABC):
    
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

    def set_apikey(self, apikey:str) -> None:
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transclude(self, message:str) -> str:
        pass
