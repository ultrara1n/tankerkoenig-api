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

    stationData = stationJSON.get('station')
    stationName = stationData.get('name')
    stationBrand = stationData.get('brand')
    priceE5 = stationData.get('e5')
    priceE10 = stationData.get('e10')
    priceDiesel = stationData.get('diesel')
    print(stationName)
    print("Marke: " + stationBrand)
    print("E5: " + str(priceE5))
    print("E10: " + str(priceE10))
    print("Diesel: " + str(priceDiesel))
    print()


    return
