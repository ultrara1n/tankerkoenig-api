import pytankerkoenig
import os

print(pytankerkoenig.getStationData(os.environ['api_key'],'5bd71e9d-7001-4908-a29d-36c28d6eb615'))

print(pytankerkoenig.getNearbyStations(os.environ['api_key'],'50.758914','7.201223','5','all','dist'))
