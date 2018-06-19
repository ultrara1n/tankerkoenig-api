try:
    import urllib2 as request
except:
    from urllib import request

import json

def getStationData(apikey, station):
    # Build the URL with apikey and station-id to fetch station details
    stationBaseurl = "https://creativecommons.tankerkoenig.de/json/detail.php?id="
    stationFullurl = stationBaseurl + station + "&apikey=" + apikey

    #Fetch and return data
    return retrieveData(stationFullurl)

def getNearbyStations(apikey, latitude, longitude, radius, type, sort):
    # Build the URL with apikey and station-id to fetch station details
    stationBaseurl = "https://creativecommons.tankerkoenig.de/json/list.php?lat="
    stationFullurl = stationBaseurl + latitude + "&lng=" + longitude + "&rad=" + radius + "&sort=" + sort + "&type=" + type + "&apikey=" + apikey

    #Fetch and return data
    return retrieveData(stationFullurl)

def getPriceList(apikey, stationlist):
    pricelistUrl = "https://creativecommons.tankerkoenig.de/json/prices.php?apikey=" + apikey + "&ids="

    for station in stationlist:
        pricelistUrl = pricelistUrl + station + ","

    pricelistUrl = pricelistUrl[:-1]

    return retrieveData(pricelistUrl)

def retrieveData(url):
    # Fetch station details
    response = request.urlopen(url)
    # Prepare the response
    encoding = response.headers['content-type'].split('charset=')[-1]
    responseJSON = json.loads(response.read().decode(encoding))

    #Check for error in response
    if responseJSON['ok'] == False:
        raise customException(responseJSON['message'])

    return responseJSON

class customException(Exception):
    pass
