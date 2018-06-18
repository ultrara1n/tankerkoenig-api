try:
    import urllib2 as request
except:
    from urllib import request

import json

def getStationData(apikey, station):
    # Build the URL with apikey and station-id to fetch station details
    stationBaseurl = "https://creativecommons.tankerkoenig.de/json/detail.php?id="
    stationFullurl = stationBaseurl + station + "&apikey=" + apikey
    # Fetch station details
    stationResponse = request.urlopen(stationFullurl)
    # Prepare the response
    encoding = stationResponse.headers['content-type'].split('charset=')[-1]
    stationJSON = json.loads(stationResponse.read().decode(encoding))

    return stationJSON

def getNearbyStations(apikey, latitude, longitude, radius, type, sort):
    # Build the URL with apikey and station-id to fetch station details
    stationBaseurl = "https://creativecommons.tankerkoenig.de/json/list.php?lat="
    stationFullurl = stationBaseurl + latitude + "&lng=" + longitude + "&rad=" + radius + "&sort=" + sort + "&type=" + type + "&apikey=" + apikey
    # Fetch station details
    stationResponse = request.urlopen(stationFullurl)
    # Prepare the response
    encoding = stationResponse.headers['content-type'].split('charset=')[-1]
    nearbyStationsJSON = json.loads(stationResponse.read().decode(encoding))

    return nearbyStationsJSON
