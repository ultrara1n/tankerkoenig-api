try:
    import urllib2 as request
except:
    from urllib import request

import json

def getPrice(apikey, station):
    # Build the URL with apikey and station-id to fetch station details
    stationBaseurl = "https://creativecommons.tankerkoenig.de/json/detail.php?id="
    stationFullurl = stationBaseurl + station + "&apikey=" + apikey
    # Fetch station details
    stationResponse = request.urlopen(stationFullurl)
    # Prepare the response
    encoding = stationResponse.headers['content-type'].split('charset=')[-1]
    stationJSON = json.loads(stationResponse.read().decode(encoding))

    stationDict = {}

    stationData = stationJSON.get('station')
    stationDict['name'] = stationData.get('name')
    stationDict['brand'] = stationData.get('brand')
    stationDict['e5'] = stationData.get('e5')
    stationDict['e10'] = stationData.get('e10')
    stationDict['diesel'] = stationData.get('diesel')

    return stationDict
