import requests
import json

from requests import RequestException

class GeolocationParams:
    def __init__(self):
        self.__ipAddress = ""
        self.__fields = ""
        self.__excludes = ""
        self.__lang = "en"
        self.__ipAddresses = []
    
    def setIPAddress(self, ipAddress: str):
        self.__ipAddress = ipAddress
    
    def getIPAddress(self) -> str:
        return self.__ipAddress
    
    def setFields(self, fields: str):
        self.__fields = fields
    
    def getFields(self) -> str:
        return self.__fields
    
    def setExcludes(self, excludes: str):
        self.__excludes = excludes
    
    def getExcludes(self) -> str:
        return self.__excludes

    def setLang(self, lang: str = "en"):
        self.__lang = lang

    def getLang(self) -> str:
        return self.__lang

    def setIPAddresses(self, ipAddresses: [] = []):
        if len(ipAddresses) > 50:
            ValueError("Maximum number of IP addresses for bulk lookup cannot be more than 50.")
        else:
            self.__ipAddresses = ipAddresses

    def getIPAddresses(self) -> []: 
        return self.__ipAddresses
    
    def getURLParams(self) -> dict:
        urlParams = {}

        if self.__ipAddress:
            urlParams["ip"] = self.__ipAddress
        
        if self.__fields:
            urlParams["fields"] = self.__fields
        
        if self.__excludes:
            urlParams["excludes"] = self.__excludes
        
        if self.__lang:
            urlParams["lang"] = self.__lang
        
        return urlParams

class TimezoneParams:
    def __init__(self):
        self.__ipAddress = ""
        self.__timezone = ""
        self.__latitude = ""
        self.__longitude = ""
        self.__lang = "en"
    
    def setIPAddress(self, ipAddress: str):
        self.__ipAddress = ipAddress
    
    def getIPAddress(self) -> str:
        return self.__ipAddress
    
    def setTimezone(self, timezone: str):
        self.__timezone = timezone
    
    def getTimezone(self) -> str:
        return self.__timezone
    
    def setCoordinates(self, latitude: str, longitude: str):
        self.__latitude = latitude
        self.__longitude = longitude
    
    def getLatitude(self) -> str:
        return self.__latitude

    def getLongitude(self) -> str: 
        return self.__longitude

    def setLang(self, lang: str = "en"):
        self.__lang = lang

    def getLang(self) -> str:
        return self.__lang
    
    def getURLParams(self) -> dict:
        urlParams = {}

        if self.__ipAddress:
            urlParams["ip"] = self.__ipAddress
        
        if self.__latitude and self.__longitude:
            urlParams["lat"] = self.__latitude
            urlParams["long"] = self.__longitude
        
        if self.__timezone:
            urlParams["tz"] = self.__timezone
        
        if self.__lang:
            urlParams["lang"] = self.__lang
        
        return urlParams

class IPGeolocationAPI:
    def __init__(self, apiKey):
        if not apiKey:
            raise ValueError("API key is not provided.")
        else:
            self.__urlParams = {"apiKey": apiKey}
    
    def getApiKey(self):
        return self.__apiKey

    def getGeolocation(self, geolocationParams: GeolocationParams = None):
        if geolocationParams != None:
            if len(geolocationParams.getIPAddresses()) > 0:
                requestData = json.dumps({"ips": geolocationParams.getIPAddresses()})
                geolocationURLParams = geolocationParams.getURLParams()
                geolocationURLParams.update(self.__urlParams)

                return self.__post("ipgeo-bulk", requestData, geolocationURLParams)
            else:
                geolocationURLParams = geolocationParams.getURLParams()
                geolocationURLParams.update(self.__urlParams)

                return self.__get("ipgeo", geolocationURLParams)
        else:
            return self.__get("ipgeo", self.__urlParams)
    
    def getTimezone(self, timezoneParams: TimezoneParams = None):
        if timezoneParams:
            timezoneURLParams = timezoneParams.getURLParams()
            timezoneURLParams.update(self.__urlParams)
            
            return self.__get("timezone", timezoneURLParams)
        else:
            return self.__get("timezone", self.__urlParams)
        
    def __get(self, path: str, urlParams: dict = {}) -> dict:
        url = "https://api.ipgeolocation.io/{0}".format(path)
        jsonResponse = None
        
        try:
            response = requests.get(url, params=urlParams)
            jsonResponse = response.json()
            
            if response.status_code != 200:
                print("HTTP Get Request Failed: status_code={0}, response={1}".format(response.status_code, jsonResponse))
        except RequestException as e:
            print(e)
        except ValueError as e:
            print(e)
        
        return jsonResponse
    
    def __post(self, path: str, requestData: str = "", urlParams: dict = {}) -> []:
        url = "https://api.ipgeolocation.io/{0}".format(path)
        jsonResponse = None

        try:
            response = requests.post(url, params=urlParams, data=requestData)
            jsonResponse = response.json()
        
            if response.status_code != 200:
                print("HTTP Post Request Failed: status_code={0}, response={1}".format(response.status_code, jsonResponse))
        except RequestException as e:
            print(e)
        except ValueError as e:
            print(e)
        
        return jsonResponse